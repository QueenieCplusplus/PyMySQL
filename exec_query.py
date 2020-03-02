# -*- coding: utf-8 -*-
'''
Created on 2020.3.02
@author: 100900 QueenPy
'''

import datetime
from mysql_conn import create_cursor, execute_query, execute_query, close_db

query = execute_query().cc
query_result = execute_query()

def insert_2_db():

    try:
        with query as q:
            

    finally:
        close_db()

if __name__ == "__main__":
    insert_2_db()
