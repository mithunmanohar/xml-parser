"""
script name : start_process.py
created on : 1-MAY-2018
"""

__author__ = "mithun"

# Global imports
import os
import sys
import logging


# Local imports
from src.utilities import utils


# Global Constants

ZIP_FILE_LOCATION = ""

def setup_logger(log_level, log_file_path):
    """
    Sets up logger with the specified log level and log location
    Args:
        log_level : log level severity
        log_file_path : path in which log has to be created
    returns : None
    """

    logging.basicConfig(
        filename=log_file_path,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=log_level
        )

    logging.info('Initialised Logger')


def check_and_process_zip(zip_file_location):
    """
    Checks if given zip file path exists, creates a temp folder in the
    location, unzips the files to the temp folder and returns the temp
    folder path

    Args:
        zip_file_location : location of the input zip file
    Returns:
        file_path : temp location contatining unzipped files

    """

    if os.path.isdir(zip_file_location):
        pass
    else:
        logging.warning('Zip file location not found')

if __name__ == '__main__':
    setup_logger(logging.INFO, 'start_process.log')
    file_folder = check_and_process_zip(ZIP_FILE_LOCATION)