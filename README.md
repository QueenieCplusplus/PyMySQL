# SQL_App

Pymysql

![PyMySQL Engine](https://www.xzymoe.com/wp-content/uploads/2019/03/pymysql.png)

> code 


        
        import pymysql
        import pymysql.cursors
        
        # connect to DB to create session
        
        db = pymysql.connect(
            host="", #localhost
            port=3307,#3306
            user="",
            passwd="",
            db='', # DB Schema
            # interval = ping 20/sec 
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            # query = {'charset': 'utf8mb4'}
            )
        
> url


        URL(
            drivername = 'mysql+pymysql',
            host = '',
            port = 3307,
            username = '',
            password = '',
            database = '',
            query = {'charset': 'utf8mb4'}
            )
            
> Session & Connection

http://einverne.github.io/post/2017/05/sqlalchemy-session.html
            
            
> ORM model file out put


        pip install sqlacodegen 

        sqlacodegen mysql+pymysql://username:password@mysqlIP:3306/dbname --outfile filename.py

> SQL Query Statement

   使用pymysql的引數化語句防止SQL隱碼攻擊

        import pymysql
        import pymysql.cursors

        # db is sshema
        conn = pymysql.connect(host='', port=, user='queenie', passwd='queenie', db='queenie', charset='utf8mb4')

        cr = conn.cursor()

        #row = cr.executemany("insert into table_name( col1, col2, col3)values(%s, %s, %s)", [("val1", 'val2', 'val3'), ("vala", 'valb', 'valc')])
        #print(row)

        # replace %c || %i by %s
        row_show_insert = cr.execute("INSERT INTO queensTable(item, price) VALUES(%s, %s)", ('r', 5000))
        
        conn.commit()
        cr.close()
        conn.close()
        
> Avoid Duplicate Entry using INSERT IGNORE 

        import pymysql
        import pymysql.cursors
        
        # db is sshema
        conn = pymysql.connect(host='', port=, user='queenie', passwd='queenie', db='queenie', charset='utf8mb4')
        
        cr = conn.cursor()
        # to add IGNORE to avoid duplicate entry.
        # this table shall created with default field called Primary_Key
        row_show_insert_without_duplicate_entries = cr.execute("INSERT IGNORE INTO qsIDtable(tech, duration) VALUES(%s, %s)", ('android', 24))
        
        print(row_show_insert_without_duplicate_entries)
        
        conn.commit()
        cr.close()
        conn.close()

> Formatting Options


    formatting options 
 
    The others should be %s for string. 


        'c' Single character (accepts integer or single character string).
        'r' String (converts any Python object using repr()).
        's' String (converts any Python object using str()). 
        
        
'%' No argument is converted, results in a '%' character in the result.
        
|   %      |        meaning          |   alternative  |
|----------|:-----------------------:|---------------:|
| d        | Signed int decimal      |       u        |
| i        | Signed int decimal      |                |
| o        | Signed octal val        |                |
| x        | Signed Hexa decimal     |       X        |
| e        | Float point exponential |       E        |
| f        | Float point decimal     |       F        |
| g        |          (omit)         |       G        |
| c        | Single character        |     i || s     |
| s        | String                  |                |
| r        | String                  |                |

> dialects

<https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql>

> SQLAlchemy is ORM API

 ![orm](https://i2.kknews.cc/SIG=3a21e28/ctp-vzntr/043qo55068n04s6594o6r9r5s62qo93p.jpg)
 
> see sample code
 
 https://github.com/QueenieCplusplus/SQLAlchemy_app/blob/master/README.md
