"""
A program that generates pdf invoices from a csv file. 
"""
from pull_csv_data import CSVData


def main(csv_path="data/data.csv"):
    print("This is the main function.")
    csv_data = CSVData(csv_path)

    for row in csv_data:
        print(row)


if __name__ == "__main__":
    main()
