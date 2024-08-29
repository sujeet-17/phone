#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Thankq for Register</h1>")

Form=cgi.FieldStorage()
sname=Form.getvalue('name')
semail=Form.getvalue('email')
sphone=Form.getvalue('phone')
print(sname,semail,sphone)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="signin"
)

mycursor=mydb.cursor()

sql="INSERT INTO client(name,email,phone) VALUES (%s,%s,%s)"
val=(sname,sphone,semail)

mycursor.execute(sql,val)
mydb.commit()



print("</body>")
print("</html>")