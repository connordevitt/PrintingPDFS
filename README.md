# Printing PDFs

## Overview

This project automates the printing of PDF files using Adobe Acrobat DC. It walks through a specified directory, identifies PDF files, and prints them using Adobe Acrobat DC. The status of each file is logged to a log file, and a list of processed files is maintained.

## Prerequisites

- Adobe Acrobat DC installed on the system
- Python 3.x installed on the system

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/pdf-print-automation.git
   ```

## Navigate to the project directory:

cd pdf-print-automation

## Install the required dependencies:

pip install -r requirements.txt

## Configuration

1. Open the config.py file.
2. Update the pdf_files_path variable with the path to the directory containing the PDF files you want to print.
3. Update the acrobat_path variable with the path to the Adobe Acrobat DC executable on your system.
4. Update the log_file_path and processed_files_path variables with the desired paths for the log file and processed files list, respectively.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory:
```  
 cd pdf-print-automation
```

3. Run the script:
```
   python main.py
```

## Logging

The script logs the status of each file to the print_log.txt file. The log file includes information such as the start and end times of the print job, the files processed, any errors encountered, and the standard output and error from the subprocess.

## Processed Files

The script maintains a list of processed files in the processed_files.txt file. This file keeps track of the files that have been successfully printed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please reach out to connor.devitt2@gmail.com
