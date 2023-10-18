# GenBank Data Extractor

- The GenBank Data Extractor is a Python project designed to facilitate the extraction of valuable information from GenBank files (.gb) and convert it into a tabular format (CSV). This ETL (Extract, Transform, Load) process helps biologists and researchers quickly access and analyze sequence data for various biological studies, such as phylogenetic analysis.

## Table of Contents
- [About the Project](#about-the-project)
- [Problem](#problem)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Problem

- Researchers often need to analyze biological sequences by extracting essential information from GenBank files. For example:

    - Identifying the countries from which the sequences originate.
    - Determining the individuals or organizations that collected the samples.
    - Verifying whether a given sequence has been published in a scientific article.

- Manual extraction and analysis of such information from GenBank files can be time-consuming. This project aims to automate this process and provide quick access to the data in a structured format for analysis.

## About the Project

- The GenBank is a critical resource for accessing biological sequence data. However, GenBank files are typically not user-friendly and require manual inspection to find specific information. This project aims to solve that problem by automating the extraction and transformation of data from GenBank files, making it accessible and easy to analyze.

### Why is this project useful?

- Quickly identify if a biological sequence has been published in a scientific article.
- Tabulate GenBank data for easy access and analysis in spreadsheet software.
- Conduct statistical analyses, such as the number of sequences per genus and their countries of origin.
- Verify the completeness and consistency of GenBank data during the submission process.

## Features

- Extracts relevant information from GenBank files:
  - Molecule type
  - DNA region
  - Accession number
  - Organism name
  - Specimen voucher
  - Country
  - Type material
  - Isolate
  - Strain
  - Isolation source
  - Host
  - Collection date
  - Collected by
  - Identified by
  - TaxID
  - Title
  - Authors
  - Journal
  - Sequence description
  - Sequence length
  - Sequence data
- Supports GenBank files in .gb format.
- Converts the data into a CSV file for easy analysis in spreadsheet software.

## Getting Started

- To get started with the GenBank Data Extractor, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages by running: 

        
        pip install -r requirements.txt
        

## Usage

- To use the GenBank Data Extractor, you need to run the Python script with your GenBank file as input. Here's how you can do it:

        
        python3 genbank_data_extractor.py
        

- `input_genbank_file.gb` should be replaced with the path to your GenBank file.
- `output_csv_file.csv` should be replaced with the desired name for the output CSV file.

## Output

- The output is a CSV file containing tabulated data extracted from the GenBank file. You can easily open and analyze this file using spreadsheet software such as Microsoft Excel or Google Sheets.

## Contributing

- Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.

## License

- Distributed under the MIT License. See `LICENSE` for more information.
