"""NumPy fundamentals collected from my early Python learning notes."""

import numpy as np


def show_shape_and_reshape() -> None:
    values = np.arange(12)
    matrix = values.reshape(3, 4)
    print("1D shape:", values.shape)
    print("2D shape:", matrix.shape)
    print(matrix)


def show_view_and_copy() -> None:
    source = np.arange(6)
    view = source[:3]
    view[0] = 99
    print("A slice is normally a view:", source)

    copied = source[:3].copy()
    copied[0] = -1
    print("A copied slice does not modify the source:", source)


def show_broadcasting() -> None:
    matrix = np.arange(12).reshape(4, 3)
    row_offset = np.array([10, 20, 30])
    print("Broadcasting a row vector:")
    print(matrix + row_offset)


def show_boolean_mask() -> None:
    rng = np.random.default_rng(seed=42)
    samples = rng.normal(loc=0.0, scale=1.0, size=10_000)
    ratio = np.mean(np.abs(samples) < 1)
    print(f"Ratio inside one standard deviation: {ratio:.2%}")


def show_matrix_multiplication() -> None:
    left = np.arange(6).reshape(2, 3)
    right = np.arange(6).reshape(3, 2)
    print("Elementwise multiplication requires compatible shapes.")
    print("Matrix multiplication uses @ or np.matmul:")
    print(left @ right)


if __name__ == "__main__":
    show_shape_and_reshape()
    show_view_and_copy()
    show_broadcasting()
    show_boolean_mask()
    show_matrix_multiplication()

