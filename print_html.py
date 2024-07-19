import os
import subprocess
import time
import datetime
import logging


# Path to the PDF files
pdf_files_path = r'C:\Users\david\Desktop\EOBS\Strata EOBs'  # Change this to your directory path


# Path to Adobe Acrobat DC
acrobat_path = r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe'


# Log file path
log_file_path = r'C:\Users\david\Desktop\EOBS\Strata EOBs\print_log.txt'
processed_files_path = r'C:\Users\david\Desktop\EOBS\Strata EOBs\processed_files.txt'


# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_processed_file(file_path):
    with open(processed_files_path, 'a') as processed_file:
        processed_file.write(f"{file_path}\n")
    logging.info(f"Marked {file_path} as processed")


def print_pdf(file_path):
    try:
        logging.info(f"Printing {file_path}")
        if not os.path.exists(acrobat_path):
            raise FileNotFoundError(f"Adobe Acrobat executable not found at {acrobat_path}")
       
        # Use Adobe Acrobat DC to open the file for printing
        result = subprocess.run(
            [acrobat_path, '/t', file_path],
            capture_output=True,
            text=True,
            timeout=60  # Add a timeout to prevent indefinite blocking
        )
       
        # Log the standard output and error
        logging.debug(f"Standard Output: {result.stdout}")
        logging.debug(f"Standard Error: {result.stderr}")
       
        if result.returncode == 0:
            logging.info(f"Sent {file_path} to printer successfully")
        else:
            logging.warning(f"Subprocess returned non-zero exit code {result.returncode} for {file_path}")
            logging.warning(f"Subprocess error output: {result.stderr}")
            # Optionally: Add logic here to handle specific non-zero exit codes differently if needed


        # Mark the file as processed regardless of the return code
        log_processed_file(file_path)
        time.sleep(5)  # Wait a few seconds for the print job to process
    except subprocess.TimeoutExpired:
        logging.error(f"Timeout expired while printing {file_path}")
    except Exception as e:
        logging.error(f"Error printing {file_path}: {e}")


def print_documents():
    start_time = datetime.datetime.now()
    logging.info(f"Starting print job at {start_time}")
   
    processed_files = set()
    if os.path.exists(processed_files_path):
        with open(processed_files_path, 'r') as processed_file:
            processed_files = set(line.strip() for line in processed_file)
   
    for root, dirs, files in os.walk(pdf_files_path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_file = os.path.join(root, file)
                if pdf_file not in processed_files:
                    logging.info(f"Loading {pdf_file}")
                    print_pdf(pdf_file)
   
    end_time = datetime.datetime.now()
    logging.info(f"Print job completed at {end_time}")
    duration = end_time - start_time
    logging.info(f"Total duration: {duration}")


if __name__ == "__main__":
    print_documents()


#Todo: Figure out why the print_log.txt generates an error that is "2024-07-18 11:01:26 - WARNING - Subprocess returned non-zero exit code 1 for C:\Users\david\Desktop\EOBS\Strata EOBs\2024-07-18-2568986-Remits 7.17.24  (6).pdf
# Continue of line 98: 2024-07-18 11:01:26 - WARNING - Subprocess error output: