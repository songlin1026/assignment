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
    if session.get('username')==False:
        return render_template("homePage.html")
    else:
        return redirect("/member")


@app.route("/signup",methods=["POST"])
def signup():
    signupName=request.form["signup_name"]
    signupAccount=request.form["signup_account"]
    signupPassword=request.form["signup_password"]
    cursor.execute("select * from week6.user where username=%s",[signupAccount])
    data=cursor.fetchone()
    if data == None :
        cursor.execute("insert into user(name,username,password) values (%s,%s,%s) ",[signupName,signupAccount,signupPassword]) 
        connection.commit()
        return redirect("/")
    else:
        return redirect(url_for("error",message="帳號已經被註冊過了"))



@app.route("/signin",methods=["POST"])
def signin():
    signinAccount=request.form["signin_account"]
    signinPassword=request.form["signin_password"]
    cursor.execute("select * from week6.user where username=%s",[signinAccount])
    data=cursor.fetchone()
    if data != None :
        if data[3]== signinPassword :
            session['username'] = data[1]
            return redirect(url_for("member"))
        else:
            return redirect(url_for("error",message="帳號或密碼錯誤"))
    else:
        return redirect(url_for("error",message="帳號或密碼錯誤"))



@app.route("/member")
def member():
    if session.get('username') == False :
        return redirect("/")
    else:
        member=session.get('username')
        cursor.execute("select * from week6.user where name=%s",[member])
        data=cursor.fetchone()
        return render_template("member.html",name=data[1])


@app.route("/signout")
def signout():
    session['username'] = False
    return render_template("signout.html")


@app.route("/error/")
def error():
    if session.get('username') != False :
        member=session.get('username')
        cursor.execute("select * from week6.user where name=%s",[member])
        data=cursor.fetchone()
        return redirect(url_for("member")) 
    else:
        content=request.args.get('message')
        return render_template("error.html",message=content)

app.run(port=3000)
