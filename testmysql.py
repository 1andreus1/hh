# -*- coding: utf-8 -*-
from mysql.connector import connect
dbname = 'newtest'
host = 'localhost'
user = 'admin'
password = 'admin'
conn = connect(host=host, user=user, password=password, )
cursor = conn.cursor()
cursor.execute('USE ' + dbname + ';')
sql = "SELECT * FROM datasets WHERE DatasetSource = 'yandex.maps';"
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)
#conn.commit()

