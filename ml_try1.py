import os
import pymysql.cursors
import json
variable=input("Enter your command")

#connection to the database
connectionObject=pymysql.connect(host='127.0.0.1',user='root',password='2002',database='speech_recognition',charset='utf8mb4'
,cursorclass=pymysql.cursors.DictCursor)

#creating a cursor object

try:
    cursorObject=connectionObject.cursor()

    #sql query
    var='"'+variable+'"'
    sqlQuery="select * from commands where user_input="+var
    print(sqlQuery)

    cursorObject.execute(sqlQuery)

    rows=cursorObject.fetchall()
    dict=rows[0]
    val=list(dict.values())
    command=val[0]
    print(command)
    #s=''.join(val)
    #print(s)
    #val=dict.get()
    #print(json.dumps(dict))
    #print(values)

except Exception as e:
    print("Exception Occured")

finally:
    connectionObject.close()
