# Invoice Generator

This project is a tool for generating PDF invoices from a CSV file.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Pandas library
- ReportLab library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/invoice-generator.git
    ```

2. Change into the project directory:

    ```bash
    cd invoice-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your CSV file in the project directory.

2. Run the following command to generate the invoices:

    ```bash
    python invoice_generator.py --input <csv_file> --output <output_directory>
    ```

    Replace `<csv_file>` with the name of your CSV file and `<output_directory>` with the directory where you want to save the generated invoices.

3. The PDF invoices will be generated in the specified output directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
