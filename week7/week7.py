from flask import Flask  #載入Flask模組
from flask import request #載入request物件
from flask import redirect #載入redirect 函式
from flask import render_template
from flask import session
from flask import url_for
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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#改名 api
@app.route("/api/user",methods=["POST"])
def chage():
    changeData=json.loads(request.data.decode('utf-8'))
    changeContent=changeData["name"]
    member=session.get('username')
    # 更新資料庫、session
    cursor.execute("update week6.user set name= %s where name=%s",[changeContent,member])
    connection.commit()
    session['username'] = changeContent
    # 確認是否更新資料成功、回傳結果
    member=session.get('username')
    cursor.execute("select name from week6.user where name=%s",[member])
    check=cursor.fetchone()
    if check!=None:
        return json.dumps({'ok':'true'})
    else :
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
    if session.get('username')==False:
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
    cursor.execute("select * from week6.user where username=%s",[signinAccount])
    data=cursor.fetchone()
    if data != None :
        if data[3]== signinPassword :
            session['username'] = data[1]
            return redirect(url_for("member"))
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
    if session.get('username') == False :
        return redirect("/")
        cursor.close()
    else:
        member=session.get('username')
        cursor.execute("select * from week6.user where name=%s",[member])
        data=cursor.fetchone()
        return render_template("member.html",name=data[1])
        cursor.close()

#登出頁面
@app.route("/signout")
def signout():
    session['username'] = False
    return render_template("signout.html")

#錯誤頁面
@app.route("/error/")
def error():
    if session.get('username') != False :
        member=session.get('username')
        cursor.execute("select * from week6.user where name=%s",[member])
        data=cursor.fetchone()
        return redirect(url_for("member")) 
        cursor.close()
    else:
        content=request.args.get('message')
        return render_template("error.html",message=content)
        cursor.close()

app.run(port=3000)
cursor.close()
