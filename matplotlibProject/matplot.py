"""Generate a two-dimensional wave heatmap and save it as SVG."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    x = np.linspace(0, 10, 400)
    wave = np.sin(x) * np.cos(x).reshape(-1, 1)

    figure, axis = plt.subplots(figsize=(7, 5))
    image = axis.imshow(
        wave,
        extent=[0, 10, 0, 10],
        origin="lower",
        cmap="viridis",
        aspect="auto",
    )
    axis.set_title("2D Wave Pattern")
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    figure.colorbar(image, ax=axis, label="amplitude")
    figure.tight_layout()

    output_path = Path(__file__).with_name("my_wave_plot.svg")
    figure.savefig(output_path, format="svg")
    print(f"saved: {output_path}")


if __name__ == "__main__":
    main()

