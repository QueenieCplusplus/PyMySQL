# -*- coding: utf-8 -*-
'''
Created on 2020.02.21
Modified on 2020.02.26
@author: QueenPy
'''

import os, sys
import logging, re
import time as t 
import datetime as d 
import requests as req
from urllib.parse import urlparse as p

#from io import BytesIO, StringIO

def url_convert_with_logicGate(query_key_4_test):

    # to add exception catcher, done
    try:

        # to add if-else-logicalGate, done
        # url_converter(query_sheet=query_key_4_test)
        link = url_converter(query_sheet=query_key_4_test)

        # miss xls target when its http req redirect to error page then res in 'Content-Type': 'text/html'
        # process may go on when content-type is application/vnd.ms-excel

        if link.headers['Content-Type'] == 'application/vnd.ms-excel':
            today_data = link
            print('data today')
            return today_data
            # can be return link 

        elif link.headers['Content-Type'] == 'text/html':
            yesterday_data = url_converter_yesterday(query_sheet_subtract_1day=query_key_4_test)
            print('data yesterday')
            return yesterday_data

        else:
            print('The Data Source you required from has not uodated info till now, plz retry later')
            return '' # shall not be a Null Type
        
    except req.exceptions.HTTPError as e:
        logging.error(str(e))
        return 1

def url_converter(query_sheet):

    lt = t.localtime()
    zero = 0

    # https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200224-C.xls
    # target_url = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{t[0]}/{t[0]}{zero}{t[1]}/{name}.{t[0]}{zero}{t[1]}{t[2]}-C.xls'.format(name=query_sheet, zero=zero, t=lt)
    # target_url = "https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202003/FormosaCurve.20200302-C.xls"
    target_url = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{t[0]}/{t[0]}{zero}{t[1]}/{name}.{t[0]}{zero}{t[1]}{zero}{t[2]}-C.xls'.format(name=query_sheet, zero=zero, t=lt)


    # print(target_url)

    # test print : https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200224-C.xls

    #req.headers['Accept'] = 'application/vnd.ms-excel'

    res = req.get(url=target_url, timeout=500)

    if res.status_code == 200:
       print(res.url, res.status_code)
       print(res.headers['Content-Type'], res.headers['Date'])
       return res

    elif res.status_code == 404:
        print('not found, 404')

    else:
        print('you got nothing, plz check url asap!')


# param may be query_sheet, as a polymorphism
def url_converter_yesterday(query_sheet_subtract_1day):
    # to do yesterday

    y_d =d.date.today() + d.timedelta(-1) # arg of timedelta is days
    #print('yesterday is', y_d)

    # using .strftime()
    y_Y, y_M, y_D = y_d.strftime("%Y"), y_d.strftime("%m"), y_d.strftime("%d")
    #print(y_Y, y_M, y_D)

                  # https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200225-C.xls
    target_url_y = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{y_y}/{y_y}{y_m}/{name}.{y_y}{y_m}{y_d}-C.xls'.format(name=query_sheet_subtract_1day, y_y=y_Y, y_m=y_M, y_d=y_D)

    res = req.get(url=target_url_y, timeout=600)

    if res.status_code == 200:
        print(res.url, res.status_code)
        print(res.headers['Content-Type'], res.headers['Date'])
        print(type(res.content)) #<class 'bytes'>
        return res

    elif res.status_code == 404:
        print('not found, 404')

    else:
        print('you got nothing, plz check url asap!')

    # application/vnd.ms-excel Wed, 26 Feb 2020 02:10:56 GMT

    # query_file = ''
    #local_time = t.localtime()
    #q_y = local_time[0]
    #q_m = local_time[1]
    #q_d =  local_time[2]

    #if query_file == 'bond_curve_today':

        #local_time = t.localtime()
        #q_y = local_time[0]
        #q_m = local_time[1]
        #q_d =  local_time[2]

        # https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200221-C.xls
        #target_url = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//{q.y}/{q.y}{q.m}/FormosaCurve.{q.y}{q.m}{q.d}-C.xls'
        #content_type = 'application/vnd.ms-excel'

        #res = req.get(url=target_url, timeout=300)
        #logging.INFO('aim at xls dw page and status code is', res.status_code)
        #print(target_url, res.status_code)
        #return target_url

        # res = req.get(target_url)
        # print(res.content) #binary data type
        # 4\xbb\xa5\xe4\xb8\x8a\xe3\x80\x82 \r\n

        # .json() result in json obj
        # raise JSONDecodeError("Expecting value", s, err.value) from None
        # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    
    #else:

        #alter_to_url = 'https://www.tpex.org.tw/web/bond/tradeinfo/internationalbond/FormosaDaily.php?l=zh-tw'
        #res = req.get(url=alter_to_url, timeout=100)
        #print('back to main page', res.status_code)

if __name__ == "__main__":

    # query_word = 'bond_curve_today'
    ## html_converter(query_file=query_word)
    ## html_converter()
    query_key_4_test = 'FormosaCurve'
    # if file nit post today, then the req will be redirect , and status code will be 300   

    url_convert_with_logicGate(query_key_4_test) 
