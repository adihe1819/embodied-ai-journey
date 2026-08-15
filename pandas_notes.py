"""Small, self-contained Pandas examples for tabular data analysis."""

import pandas as pd


def make_demo_data() -> pd.DataFrame:
    """Return a tiny synthetic passenger table, not the real Titanic dataset."""
    return pd.DataFrame(
        {
            "survived": [1, 0, 1, 1, 0, 0, 1, 0],
            "sex": ["female", "male", "female", "male"] * 2,
            "age": [16, 22, 35, 47, 12, 66, 29, 41],
            "fare": [72.0, 8.1, 53.2, 13.0, 31.0, 7.8, 80.0, 26.0],
            "class": [1, 3, 1, 2, 2, 3, 1, 2],
        }
    )


def survival_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """Compare survival rate across several categorical groups."""
    working = frame.copy()
    working["age_group"] = pd.cut(
        working["age"], bins=[0, 18, 40, 120], labels=["child", "adult", "older"]
    )
    working["fare_group"] = pd.qcut(
        working["fare"], q=3, labels=["low", "medium", "high"]
    )

    return working.pivot_table(
        values="survived",
        index=["class", "fare_group"],
        columns=["sex", "age_group"],
        aggfunc="mean",
        observed=True,
    )


if __name__ == "__main__":
    data = make_demo_data()
    print("Preview:")
    print(data.head())
    print("\nShape:", data.shape)
    print("\nSurvival-rate pivot table:")
    print(survival_summary(data))

