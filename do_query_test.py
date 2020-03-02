# _*_ coding:utf-8 _*_

import pymysql
import pymysql.cursors

# db is sshema
conn = pymysql.connect(host='', port=, user='queenie', passwd='queenie', db='queenie', charset='utf8mb4')

cr = conn.cursor()

# query for update info
#row1 = cr.execute("update table_name set col_name = 'new_val'")
#print(row1)

#row_show_uodate = cr.execute("update queensTable set item='b'")
#print(row_show_uodate)

# %d for decimal or %i for integer
#row2 = cr.execute(" %s", )
#print(row2)

# query for insert info
# 使用pymysql的引數化語句防止SQL隱碼攻擊
#row3 = cr.executemany("insert into table_name( col1, col2, col3)values(%s, %s, %s)", [("val1", 'val2', 'val3'), ("vala", 'valb', 'valc')])
#print(row3)

# replace %c || %i by %s.
row_show_insert = cr.execute("INSERT INTO queensTable(item, price) VALUES(%s, %s)", ('r', 5000))
print(row_show_insert)
#TypeError: %i format: a number is required, not str

# to add IGNORE to avoid duplicate entry.
row_show_insert_without_duplicate_entries = cr.execute("INSERT IGNORE INTO qsIDtable(tech, duration) VALUES(%s, %s)", ('android', 24))
print(row_show_insert_without_duplicate_entries)

# another coding way, using varibale assignment
query_select = "SELECT * FROM rating_yield_curve"
row_show_all = cr.execute(query_select)
print(row_show_all)

conn.commit()
cr.close()
conn.close()

# pymysql.err.ProgrammingError: (1146, "Table 'queenie.queesTable' doesn't exist")