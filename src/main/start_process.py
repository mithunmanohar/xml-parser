"""
script name : start_process.py
created on : 1-MAY-2018
"""

__author__ = "mithun"

# Global imports
import os
import sys
import glob
import xlrd
import xlwt
import logging
import xml.etree.ElementTree as et


# Local imports
from src.utilities import utils



# Global Constants
def get_data_from_xml(xml_file_path, search_item):
    print xml_file_path, search_item
    e = et.parse(xml_file_path).getroot()
    print e.tag


def generate_report(unzip_folder_path, input_excel_file):
    xml_report = "report.xlsx"
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("report")

    search_list = utils.read_excel(input_excel_file)

    if len(search_list) > 0:
        logging.info('Found %f search criterias' % len(search_list))
        xml_file_list = glob.glob(unzip_folder_path + os.sep + '*.xml')
        report_data = []
        for item in search_list:
            xml_file_path = unzip_folder_path + os.sep +'cpc-scheme-' + \
                            item.split('/')[0][0:4] + '.xml'
            if os.path.exists(xml_file_path):
                data = get_data_from_xml(xml_file_path, item)
                report_data.append(data)
            break

     #   for i, l in enumerate(report_data):
      #      for j, col in enumerate(l):
       #         sheet.write(i, j, col)
        book.save("report.xlsx")
    else:
        logging.warning('No search criteria found from excel')

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
        logging.info('Created unzip folder %s ' % unzip_file_folder )
        os.mkdir(unzip_file_folder)

    unzip_folder_path = utils.unzip_files(zip_file_folder,
                                     unzip_file_folder)
    #xml_file_list = glob.glob(unzip_folder_path + os.sep + '*.xml')
    logging.info('Successfully extracted xml files')
    return unzip_folder_path

if __name__ == '__main__':

    input_zip_file_folder = r'F:\usefuk\fiverr\may2018\jaboo\xml-parser\input_zip'
    input_excel_file = r'F:\usefuk\fiverr\may2018\jaboo\xml-parser\input_excel\classificationsymbols20180430.xlsx'

    utils.setup_logger(logging.INFO, '../../logs/start_process.log')
    xml_file_folder = check_and_process_zip(input_zip_file_folder)

    generate_report(xml_file_folder, input_excel_file)
