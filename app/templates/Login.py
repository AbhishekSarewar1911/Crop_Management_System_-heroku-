from crypt import methods
from flask import Flask, render_template, redirect, url_for, request
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

myapp = Flask(__name__)
def homepage():
    return render_template("homepage.html")

@myapp.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['username']
    PW = request.form['password']

    sqlconnection = sqlite3.Connection(currentlocation+ "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT username, Password From Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows)==1:
        return render_template("Loggedin.html")
    else:
        return render_template("/register")

@myapp.route("/register", methods= ["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['DUsername']
        dPW = request.form['DPassword']
        Uemail = request.form['Emailuser']
        sqlconnection = sqlite3.Connection(currentlocation+ "\Login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u = dUN, p = dPW, e = Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("Register.html")


if __name__ == '__main__':
    myapp.run()