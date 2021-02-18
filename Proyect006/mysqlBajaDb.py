import mysql.connector
import csv

table1 = "polls_dccdepts"
table2 = "polls_dccusers"
table3 = "polls_dccprocs"


mydb = mysql.connector.connect(
  host="localhost",
  user="diego",
  password="rojo6667",
  database ="dccCertificados"
)

#print(mydb)
##########################################


cursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM " + table1
cursor.execute(sql)
rows = cursor.fetchall()
#for row in rows:
#    row["col"]
dict_db=rows[0]


with open('dccDepts.new.csv', 'w') as f:
   w = csv.DictWriter(f,dict_db.keys())
   w.writeheader()
   w.writerows(rows)
   f.close()


############################################


cursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM "+ table2
cursor.execute(sql)
rows = cursor.fetchall()
#for row in rows:
#    row["col"]
dict_db=rows[0]

#print(dict_db.keys())

with open('dccUsers.new.csv', 'w') as f:
    w = csv.DictWriter(f,dict_db.keys())
    w.writeheader()
    w.writerows(rows)
    f.close()



############################################


cursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM "+table3
cursor.execute(sql)
rows = cursor.fetchall()
#for row in rows:
#    row["col"]
dict_db=rows[0]

#print(dict_db.keys())

with open('dccCertificados.new.csv', 'w') as f:
    w = csv.DictWriter(f,dict_db.keys())
    w.writeheader()
    w.writerows(rows)
    f.close()

