import pandas as pd


def main():
    df = pd.read_csv('prices.txt', sep=" ", names=['Ticker', 'Min', 'Max'])

    print(df)


if __name__ == "__main__":
    main()
