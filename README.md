# OpenSource EOL Checker

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

This Python program fetches information about open-source components that have reached their end of life (EOL) from the [endoflife.date](https://endoflife.date) API. It provides a comprehensive list of EOL details for various open-source projects and exports the data to an Excel spreadsheet for easy analysis.

## Features

- **Data Retrieval**: Utilizes the endoflife.date API to fetch information on open-source components.
- **Excel Export**: Generates an Excel spreadsheet with details such as product name, life cycle, and EOL date.
- **Customizable**: Easily adaptable for different use cases and integration into other projects.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/SCR1P7K1DD13/OpenSource-EOL-Checker.git
   cd OpenSource-EOL-Checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:

   ```bash
   python endoflife.py
   ```

   The program will fetch EOL information and export it to an Excel file (`output.xlsx` by default).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [endoflife.date](https://endoflife.date) for providing the EOL API.
- [tqdm](https://github.com/tqdm/tqdm) for the progress bar functionality.

Feel free to contribute, report issues, or suggest improvements!
