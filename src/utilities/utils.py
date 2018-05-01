# -*- coding: utf-8 -*-
"""
script name : start_process.py
created on : 1-MAY-2018
"""

# Global imports
import os
import sys
import zipfile
import logging

# Local imports


def setup_logger(log_level, log_file_path):
    """
    Sets up logger with the specified log level and log location
    Args:
        log_level : log level severity
        log_file_path : path in which log has to be created
    returns : None
    """
    if os.path.exists(os.path.dirname(log_file_path)):
        pass
    else:
        os.mkdir(os.path.dirname(log_file_path))

    logging.basicConfig(
        filename=log_file_path,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=log_level
        )

    logging.info('Initialised Logger')

def read_excel(file_path, mode):
    pass

def unzip_files(zip_file_path):
    """
    Validates zip file, unzips it to a temp folder and returns list of files,
    folder path of unzipped files

    Args:
        zip_file_path
    retruns:
        folder path : location of unzipped files
        file list : list of files unzipped
    """

    print dir(zipfile)
    if zipfile.is_zipfile(zip_file_path):
        logger.info("Found a ")