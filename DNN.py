"""A small, reproducible DNN classification experiment.

The task is adapted from my original PyTorch notes: three random features are
classified by the interval containing their sum. The script is intentionally
small so that the complete data -> model -> training -> evaluation pipeline is
easy to inspect.
"""

from __future__ import annotations

import argparse
import random

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset, random_split


SEED = 42


def set_seed(seed: int = SEED) -> None:
    """Make the experiment as reproducible as practical."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def make_dataset(sample_count: int = 6_000) -> TensorDataset:
    """Create a synthetic three-class dataset."""
    features = torch.rand(sample_count, 3)
    feature_sum = features.sum(dim=1)

    # Class 0: sum < 1; class 1: 1 <= sum < 2; class 2: sum >= 2.
    labels = torch.where(
        feature_sum < 1,
        torch.zeros_like(feature_sum, dtype=torch.long),
        torch.where(
            feature_sum < 2,
            torch.ones_like(feature_sum, dtype=torch.long),
            torch.full_like(feature_sum, 2, dtype=torch.long),
        ),
    )
    return TensorDataset(features, labels)


class DNN(nn.Module):
    """A compact multilayer perceptron for the synthetic task."""

    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 3),
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.net(inputs)


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    """Return classification accuracy on a data loader."""
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for features, labels in loader:
            features = features.to(device)
            labels = labels.to(device)
            predictions = model(features).argmax(dim=1)
            correct += (predictions == labels).sum().item()
            total += labels.numel()

    return correct / total


def train(epochs: int, batch_size: int, learning_rate: float) -> float:
    """Train the model and return final test accuracy."""
    set_seed()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataset = make_dataset()

    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size
    generator = torch.Generator().manual_seed(SEED)
    train_data, test_data = random_split(
        dataset, [train_size, test_size], generator=generator
    )

    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

    model = DNN().to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    print(f"device={device} train={train_size} test={test_size}")
    for epoch in range(1, epochs + 1):
        model.train()
        loss_sum = 0.0

        for features, labels in train_loader:
            features = features.to(device)
            labels = labels.to(device)

            logits = model(features)
            loss = loss_fn(logits, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_sum += loss.item() * labels.size(0)

        if epoch == 1 or epoch % 10 == 0 or epoch == epochs:
            average_loss = loss_sum / train_size
            accuracy = evaluate(model, test_loader, device)
            print(
                f"epoch={epoch:03d} loss={average_loss:.4f} "
                f"test_accuracy={accuracy:.2%}"
            )

    return evaluate(model, test_loader, device)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    final_accuracy = train(args.epochs, args.batch_size, args.learning_rate)
    print(f"final_test_accuracy={final_accuracy:.2%}")
