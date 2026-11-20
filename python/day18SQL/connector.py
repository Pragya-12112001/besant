import mysql.connector

con = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '12345',
  database = 'college'
)

# cursor used 

if con.is_connected():
  print('connected to MYSQL successfully!!')
  
cur = con.cursor()
# sql = "INSERT INTO students(id, name, marks) VALUES(%s, %s, %s)"
# values = (103, 'Ash', 45)


# update
# sql = 'update students set marks=%s where id=%s'
# values = (89, 103)


# delete
sql = 'delete from students where id=%s'
values = (103,)

cur.execute(sql, values)
con.commit()

cur.execute('select * from students')

records = cur.fetchall()
for i in records:
  print(i)


cur.close()
con.close()