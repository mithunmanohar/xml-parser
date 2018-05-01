"""
script name : start_process.py
created on : 1-MAY-2018
"""

__author__ = "mithun"

# Global imports
import os
import sys
import xlrd
import xlwt
import logging


# Local imports
from src.utilities import utils


# Global Constants

ZIP_FILE_LOCATION = ""




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
        print dir(zip)
    else:
        logging.error('Zip file location not found')
    #file_list, file_location = utils.unzip()

if __name__ == '__main__':
    utils.setup_logger(logging.INFO, '../../logs/start_process.log')
    file_folder = check_and_process_zip(ZIP_FILE_LOCATION)