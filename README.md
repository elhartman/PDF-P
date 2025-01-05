# SEO Report Generator

This program provides a user-friendly interface for generating client-ready PDF reports from CSV files exported using the Screaming Frog SEO software.

## Features
- Easy-to-use graphical interface (built with Tkinter)
- Accepts CSV reports exported from Screaming Frog SEO
- Automatically generates neatly formatted PDF reports for clients
- Saves time by automating the report creation process

## Requirements
- Python 3.7 or higher
- Dependencies listed in `requirements.txt`:
  - `fpdf`
  - `pandas`

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/elhartman/PDF-P/
   cd PDF-P
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python pdf-p.py
   ```

2. Use the graphical interface to:
   - Select a Screaming Frog CSV report file.
   - Generate a formatted PDF report.

3. The PDF will be saved in the specified location, ready to send to clients.

## Notes
- Ensure the CSV file is properly exported from Screaming Frog SEO to avoid errors.
- For any issues or feature requests, feel free to open an issue in the repository.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
Ethan L. Hartman

