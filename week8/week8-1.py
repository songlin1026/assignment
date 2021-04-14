from flask import Flask  #載入Flask模組
from flask import request #載入request物件
from flask import redirect #載入redirect 函式
from flask import render_template
from flask import session
from flask import url_for
from flask import make_response,Response
import json
import mysql.connector
import getpass
import random, string



#mysql.connector
password=getpass.getpass(prompt='請輸入資料庫密碼: ', stream=None)
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password= password,
    database='week6',
    charset='utf8')
cursor=connection.cursor()
cursor.execute("select * from week6.user ")  #執行SQL
data=cursor.fetchall()
username_arr=None
password_password=None

app=Flask(__name__,static_folder="public",static_url_path="/")


@app.route("/")
def homePage():
    if request.cookies.get("week8") == None:
        return render_template("homePage.html")
    else:
        return redirect("/member")

@app.route("/signin",methods=["POST"])
def logIn():
    signinAccount=request.form["signin_account"]
    signinPassword=request.form["signin_password"]
    if signinAccount=="" or signinPassword=="":
        return redirect(url_for("error",message="帳號或密碼不能為空白"))
    else:
        # 開始登入
        cursor.execute("select * from week6.user where username=%s",[signinAccount])
        data=cursor.fetchone()
        # 查詢資料庫是否有此帳號
        if data != None :
            # 查詢使用者輸入的密碼是否與資料庫相符
            if data[3]== signinPassword :
                    secret_key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
                    resp=make_response(redirect(url_for("member")))
                    resp.set_cookie(key="week8",value=secret_key,expires=None)
                    return resp
                    cursor.close()
            else:
                return redirect(url_for("error",message="帳號或密碼錯誤"))
                cursor.close()
        else:
            return redirect(url_for("error",message="帳號或密碼錯誤"))

@app.route("/member")
def member():
    # 檢查是否有登入過
    if request.cookies.get("week8") == None :
        return redirect("/")
        cursor.close()
    else:
        return render_template("member.html")
        cursor.close()

@app.route("/error")
def error():
    # 檢查是否為會員
    if request.cookies.get("week8") != None :
        return redirect(url_for("member")) 
        cursor.close()
    else:
        content=request.args.get('message')
        return render_template("error.html",message=content)
        cursor.close()


@app.route("/signout")
def signout():
    # 登出並刪除cookie
    resp=make_response(render_template("signout.html"))
    resp.set_cookie(key="week8",value="",expires=0)
    return resp

app.run(port=3000)