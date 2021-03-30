from flask import Flask  #載入Flask模組
from flask import request #載入request物件
from flask import redirect #載入redirect 函式
from flask import render_template
from flask import session
from flask import url_for
import mysql.connector

#mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdzxc980899",
    database='week6',
    charset='utf8')
cursor=connection.cursor()
cursor.execute("select * from week6.user ")  #執行SQL
data=cursor.fetchall()
username_arr=None
password_password=None

#flask
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def hmoepage():
    if session.get('username')=='member':
        return redirect("/member")
    return render_template("homePage.html")


@app.route("/signup",methods=["POST"])
def signup():
    cursor.execute("select * from week6.user ")
    data=cursor.fetchall()
    signupName=request.form["signup_name"]
    signupAccount=request.form["signup_account"]
    signupPassword=request.form["signup_password"]
    x=0
    while x<len(data):
        username_arr=data[x][2]
        password_arr=data[x][3]
        if signupAccount==username_arr:
            return render_template("error.html",name="此帳號已經被註冊")
        else:
            x+=1
    cursor.execute("insert into user(name,username,password) values (%s,%s,%s) ",[signupName,signupAccount,signupPassword]) 
    connection.commit()
    return redirect("/")


@app.route("/signin",methods=["POST"])
def signin():
    cursor.execute("select * from week6.user ")
    data=cursor.fetchall()
    account=request.form["signin_account"]
    password=request.form["signin_password"]
    n=0
    while n<len(data):
        username_arr=data[n][2]
        password_arr=data[n][3]
        name=data[n][1]
        if account==username_arr and password==password_arr:
            session['username']= data[n][1]
            return render_template("member.html",name=name)
        else:
            n+=1
    return redirect(url_for("error",name="帳號或密碼輸入錯誤"))


@app.route("/member")
def member():
    z=0
    while z<len(data):
        if session.get('username')==data[z][1]:
            return render_template("member.html",name=data[z][1])
        else:
            z+=1
    return redirect("/")


@app.route("/signout")
def signout():
    session['username'] = False
    return render_template("signout.html")


@app.route("/error")
def error():
    y=0
    while y<len(data):
        if session.get('username')==data[y][1]:
            return redirect("/member")
        else:
            y+=1
    return render_template("error.html",name="帳號或密碼輸入錯誤")

app.run(port=3000)
