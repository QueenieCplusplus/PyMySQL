# -*- coding: utf-8 -*-
'''
Created on 2020.02.20

@author: QueenPy
'''
import os, sys, logging
import wget
import requests
from io import BytesIO, StringIO
from urllib.parse import urlparse
import pandas as pd

def download_tpex_bond_excelfile(url):
    # query_date=pd.Timestamp.now()
    # store_local=True

    #url = 'https://nweb.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{date.year}/{date.rear}{date.month:02}/{name}.{date.year}{date.month:02}{date.day:02}-c.xls'.format(name=name, date=query_date)

    # to do a custom header
    req_header = {'content_type' : 'application/vnd.ms-excel'}
    
    # to do a custom header with param
    req_param = {'data_date': '20200219'}


    #if-else to pass in the sheet_name as name and query_date as date in URL get process

    try:
        res = requests.get(url=target_url, headers = req_header, params = req_param)
        print(res.status_code, res.text, res.content)


    except requests.exceptions.HTTPError as e:
        logging.error(str(e))   
 
    new_bond_px = wget.download(url, 'c:/Users/109009/Downloads/new_bond.xls')

    print(new_bond_px)

if __name__ == "__main__":

    target_url = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200219-C.xls'

    # name = FormosaCurve, can be pass to the url param
    # target_url = 'https://nweb.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{date.year}/{date.rear}{date.month:02}/{name}.{date.year}{date.month:02}{date.day:02}-c.xls'.format(name=name, date=query_date)

    getRes = download_tpex_bond_excelfile(target_url)

    print(getRes)
    #python -m download_bond_excel_data
    #result is (True, <_io.BytesIO object at 0x000001EB647ED468>)
    # requirs panda tool to do parsing
