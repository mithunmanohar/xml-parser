"""
script name : start_process.py
created on : 1-MAY-2018
"""

__author__ = "sam"

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


def get_data_from_xml(xml_file_path, search_item):

    e = et.parse(xml_file_path)
    search_res = []
    for each in e.iter():
        print search_item
        if (search_item.strip() == each.attrib.get('sort-key', None) and
            each.attrib.get('level', 'na') != "6"):
            print '++++', each.attrib.get('sort-key', None)
            #and each.attrib.get('level', 'na') != "na"):
            search_res.append(search_item)
            search_res.append(each.attrib.get('level', 'na'))
            search_res.append(each.attrib.get('definition-exists', 'na'))
            search_res.append(each.attrib.get('date-revised', 'na'))
            for k in each:
                if k.tag == 'class-title':
                    title = ""
                    for tags in k:
                        if tags.tag == 'title-part':
                            for tg in tags:
                                if tg.tag == "CPC-specific-text":
                                    for tk in tg:
                                        if tk.text:
                                            if len(title) > 0:
                                                title = tk.text + ';' + title
                                            else:
                                                title = (tk.text).strip()
                                elif tg.text:
                                    if len(title) > 0:
                                        title = tg.text + ';' + title
                                    else:
                                        title = (tg.text).strip()
                    if len(title.strip()) == 0:
                        search_res.append("na")
                    else:
                        search_res.append(title)
            if len(search_res) < 5:
                search_res.append('na')
            return search_res
        elif (search_item.strip() == each.attrib.get('sort-key', None) and
            each.attrib.get('level', 'na') == "6" ):
            print '----', each.attrib.get('sort-key', None)

            search_res.append(search_item)
            search_res.append(each.attrib.get('level', 'na'))
            search_res.append(each.attrib.get('definition-exists', 'na'))
            search_res.append(each.attrib.get('date-revised', 'na'))
            for k in each:
                if k.tag == 'class-title':
                    title = ""
                    for tags in k:
                        if tags.tag == 'title-part':
                            for tg in tags:
                                if tg.tag == "CPC-specific-text":
                                    for tk in tg:
                                        if tk.text:
                                            if len(title) > 0:
                                                title = tk.text + ';' + title
                                            else:
                                                title = (tk.text).strip()
                                elif tg.text:
                                    if len(title) > 0:
                                        title = tg.text + ';' + title
                                    else:
                                        title = (tg.text).strip()

                    if len(title.strip())== 0:
                        search_res.append("na")
                    else:
                        search_res.append(title)
                if len(search_res) < 5:
                    search_res.append('na')
                    print '++++++++++'
                return search_res



def generate_report(unzip_folder_path, input_excel_file, output_excel_report):
    print '[INFO] Started generate report'
    book = xlwt.Workbook()
    sheet = book.add_sheet("report")

    search_list = utils.read_excel(input_excel_file)

    if len(search_list) > 0:
        print '[INFO] Found search list from excel'
        logging.info('Found %f search criterias' % len(search_list))
        xml_file_list = glob.glob(unzip_folder_path + os.sep + '*.xml')
        report_data = []
        print '[INFO] Found xml file list'
        for item in search_list:

            xml_file_path = unzip_folder_path + os.sep +'cpc-scheme-' + \
                            item.split('/')[0][0:4] + '.xml'
            if os.path.exists(xml_file_path):
                data = get_data_from_xml(xml_file_path, item)

                if data:
                    report_data.append(data)
        sheet.write(0, 0, "Sort Key")
        sheet.write(0, 1, "Level")
        sheet.write(0, 2, "Definition Exists")
        sheet.write(0, 3, "Date revised")
        sheet.write(0, 4, "Title Part")
        #for each in report_data:
        #    print each
        for i, l in enumerate(report_data):
            for j, col in enumerate(l):
                sheet.write(i+1, j, col)
        book.save(output_excel_report)
        print '[INFO] Report successfully saved to %s' % output_excel_report
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

    root_folder = r'F:\usefuk\fiverr\may2018\jaboo\xml-parser'

    input_zip_file_folder = root_folder + os.sep + r'input_zip'

    input_excel_file = root_folder + os.sep + r'input_excel\classificationsymbols20180430.xlsx'

    output_excel_report = root_folder + os.sep + r'output_excel\report.xls'

    sys.path.insert(0, root_folder)
    utils.setup_logger(logging.INFO, '../../logs/start_process.log')

    xml_file_folder = check_and_process_zip(input_zip_file_folder)

    generate_report(xml_file_folder, input_excel_file, output_excel_report )
