import pymysql


connection=pymysql.connect(
    host="localhost",
    user="root",
    password="asdzxc980899",
    database='week6',
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8')
cursor=connection.cursor()
# cursor.execute("select * from week6.user ")  #執行SQL
# data=cursor.fetchall()

#檢查是否註冊過
# n=0
# answer='test'
# while n<len(data):
#     username_arr=data[n]['username']
#     if answer==username_arr :
#         print("yes")
#         break
#     else:
#         n+=1
# try:
cursor.execute("insert into user(name,username,password) values ('python','python','python') ",[,]) 
connection.commit()

# except:
#     cursor.rollback()




# if answer==result :
#     print("yes")

# connection.close() #關閉資料庫
# connection.commit()  修改資料