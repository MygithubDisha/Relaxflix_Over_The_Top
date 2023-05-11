#!C:/Users/nitig/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi

print("<h1>Welcome </h1>")
print("<body bgcolor='blue'>")

form=cgi.FieldStorage()

username=form.getvalue("username")
usermail=form.getvalue("usermail")
password=form.getvalue("password")
repeatP=form.getvalue("repeatP")

import mysql.connector
con = mysql.connector.connect(user='root',password='',host='localhost',database='webpython')
cur=con.cursor()

cur.execute("insert into student values(%s,%s,%s,%s)",(username,usermail,password,repeatP))
con.commit()

cur.close()
con.close()
print("<h3>Done successfully</h3>")
# print("<a href='http://localhost/Login/Signup.html'>click here to go back</a>")