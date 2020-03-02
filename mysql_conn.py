# -*- coding: utf-8 -*-
'''
Created on 2020.3.02
@author: 100900 QueenPy
'''

import pymysql
import pymysql.cursors
import datetime


# connect to DB to create session
db = pymysql.connect(
    host="", #localhost
    port=,#3306
    user="queenie",
    passwd="queenie",
    db='queenie', # DB Schema
    # interval = ping 20/sec 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    # query = {'charset': 'utf8mb4'}
)

yesyerday = datetime.now.date() - datetime.timedelta(days=1)
today = datetime.now().date()

# param shall add the port & db_name
# param shall add query = {'charset': 'utf8mb4'}

print(db)

# to execute a sql query
def create_cursor():
    cursor = db.cursor
    print("cursor is created now. Enjoy your DB query")

def execute_query():
    cc = create_cursor()
    db_version_code = cc.execute("SELECT VERSION()")
    print("the cursor is doing sql query called SELECT")
    print("the db vesion is %s" % db_version_code)

def fetch_data():
    cc = create_cursor()
    data_fetched = cc.fetchone()
    print (data_fetched)

def close_db():
    db.close()
    print("DB request is closed now.")

if __name__ == "__main__":
    create_cursor()
    execute_query()
    #fetch_data()
    close_db()

# pymysql.err.OperationalError: 
# (2003, "Can't connect to MySQL server on 'localhost' 
# ([WinError 10061] 無法連線
# 因為目標電腦拒絕連線
# 。)")

# SOLUTION:
# 點開設定-->代理設定-->彈出Internet屬性-->區域網設定-->自動檢測設定-->重啟即可