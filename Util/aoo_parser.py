# -*- coding: utf-8 -*-
'''
Created on 2020.02.20

@author: QueenPy
'''
from pyexcel_ods import get_data
#from download_bondData_excelToAoo import new_bond_px
#ImportError: cannot import name 'new_bond_px' from 'download_bondData_excelToAoo'
import os
#using its path method to make path param not a hard code

def parse_bondInfo_aoo_file(path):

    aoo_sheet = get_data(path) 
    #curve_data = aoo_sheet['table_name'][row_number]
    curve_data = aoo_sheet['FormosaCurve'][3:4]
    print(curve_data)


if __name__ == "__main__":

    temp_path = r'C:\Users\109009\Downloads\new_bond.xls'
    xlsToAoo = temp_path.replace('xls', 'ods')
    # raise BadZipFile("File is not a zip file")
    # zipfile.BadZipFile: File is not a zip file


    # (to do) to do a if-else statement to check the file is already downloaded or not.
    parse_bondInfo_aoo_file(xlsToAoo)
