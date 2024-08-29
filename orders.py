#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Thankq for Register</h1>")

Form=cgi.FieldStorage()
sname=Form.getvalue('name')
sphone=Form.getvalue('phone')
semail=Form.getvalue('email')
saddress=Form.getvalue('address')
smodel=Form.getvalue('model')
print(sname,sphone,semail,saddress,smodel)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="phone"
)

mycursor=mydb.cursor()

sql="INSERT INTO customer(name,phone,email,address,model) VALUES (%s,%s,%s,%s,%s)"
val=(sname,sphone,semail,saddress,smodel)

mycursor.execute(sql,val)
mydb.commit()



print("</body>")
print("</html>")