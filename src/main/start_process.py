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

ZIP_FILE_FOLDER = r'F:\usefuk\fiverr\may2018\jaboo\xml-parser\input_zip'




def check_and_process_zip(zip_file_folder):
    """
    Checks if given zip file path exists, creates a temp folder in the
    location, unzips the files to the temp folder and returns the temp
    folder path

    Args:
        zip_file_location : location of the input zip file
    Returns:
        file_path : temp location contatining unzipped files

    """

    if os.path.isdir(zip_file_folder):
        logging.info('ZIP file folder exists')
    else:
        logging.error('Zip file folder do not exist')

    unzip_file_folder = zip_file_folder + os.sep + 'temp'

    if not os.path.exists(unzip_file_folder):
        logging.info('Created unzip folder %s ' %s unzip_file_folder )
        os.mkdir(unzip_file_folder)

    file_list, file_location = utils.unzip_files(zip_file_folder,
                                                 unzip_file_folder)

if __name__ == '__main__':
    utils.setup_logger(logging.INFO, '../../logs/start_process.log')
    file_folder = check_and_process_zip(ZIP_FILE_FOLDER)