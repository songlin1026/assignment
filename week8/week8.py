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

#flask
app=Flask(__name__,static_folder="public",static_url_path="/")


#改名 api
@app.route("/api/user",methods=["POST"])
def chage():
    changeData=json.loads(request.data.decode('utf-8'))
    changeContent=changeData["name"]
    member=request.cookies.get("week8")
    try:
        # 更新資料庫、cookie
        cursor.execute("update week6.user set name= %s where name=%s",[changeContent,member])
        connection.commit()
        resp=make_response(json.dumps({'ok':'true'}))
        resp.set_cookie(key="week8",value=changeContent,expires=None)
        return  resp
    except:
        return json.dumps({'error':'true'})

#查詢 api
@app.route("/api/users",methods=["GET"])
def search():
        searchAccount=request.args.get("username","")
        cursor.execute("select * from week6.user where username=%s",[searchAccount])
        memberData=cursor.fetchone()
        # 查詢是否為會員
        if memberData != None:
            dataJson={"id":memberData[0],"name":memberData[1],"username":memberData[2]}
            webData={"data":dataJson}
            webData2=json.dumps(webData,indent=4,ensure_ascii=False)
            return webData2
            cursor.close()
        else:
            noneJson={}
            noneData={"data":None}
            noneData2=json.dumps(noneData,indent=4,ensure_ascii=False)
            return noneData2
            cursor.close()

#首頁
@app.route("/")
def hmoepage():
    if request.cookies.get("week8") == None:
        return render_template("homePage.html")
        cursor.close()
    else:
        return redirect("/member")
        cursor.close()

#註冊
@app.route("/signup",methods=["POST"])
def signup():
    signupName=request.form["signup_name"]
    signupAccount=request.form["signup_account"]
    signupPassword=request.form["signup_password"]
    # 查詢前端傳來資料是否為空白
    if signupName==""or signupAccount==""or signupPassword=="":
        return redirect(url_for("error",message="資料欄位有空白無法註冊帳號"))
    else:
        # 開始註冊
        cursor.execute("select * from week6.user where username=%s",[signupAccount])
        data=cursor.fetchone()
        if data == None :
            cursor.execute("insert into user(name,username,password) values (%s,%s,%s) ",[signupName,signupAccount,signupPassword]) 
            connection.commit()
            return redirect("/")
            cursor.close()
        else:
            return redirect(url_for("error",message="帳號已經被註冊過了"))
            cursor.close()


#登入
@app.route("/signin",methods=["POST"])
def signin():
    signinAccount=request.form["signin_account"]
    signinPassword=request.form["signin_password"]
    # 查詢前端傳來資料是否為空白
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
                resp=make_response(redirect(url_for("member")))
                resp.set_cookie(key="week8",value=str(data[1]),expires=None)
                return resp
                cursor.close()
            else:
                return redirect(url_for("error",message="帳號或密碼錯誤"))
                cursor.close()
        else:
            return redirect(url_for("error",message="帳號或密碼錯誤"))
            cursor.close()


#會員頁面
@app.route("/member")
def member():
    # 檢查是否有登入過
    if request.cookies.get("week8") == None :
        return redirect("/")
        cursor.close()
    else:
        member= request.cookies.get("week8")
        return render_template("member.html",name=member)
        cursor.close()

#登出頁面
@app.route("/signout")
def signout():
    # 登出並刪除cookie
    resp=make_response(render_template("signout.html"))
    resp.set_cookie(key="week8",value="",expires=0)
    return resp

#錯誤頁面
@app.route("/error/")
def error():
    # 檢查是否為會員
    if request.cookies.get("week8") != None :
        member=request.cookies.get("week8")
        return redirect(url_for("member")) 
        cursor.close()
    else:
        content=request.args.get('message')
        return render_template("error.html",message=content)
        cursor.close()

app.run(port=3000)
cursor.close()
