from pathlib import Path

import pandas as pd


def main():
    data_path = Path("data") / "supercars.csv"
    print(f"--- Loading data from {data_path} ---")
    df = pd.read_csv(data_path)
    print("--- Dataset Head ---")
    print(df.head())


if __name__ == "__main__":
    main()
