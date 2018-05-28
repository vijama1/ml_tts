import os
import pymysql.cursors
import json
insplit=[]

#Input from user via mic
user_input=input("Enter your command:")

#Invalid words which will be removed
invalid_words=['a','an','the','is','am','are','this','that','do','please','would','you','of','me','could','show','present','my','what','who','me','my','','tell','hey','all','in']



connectionObject=pymysql.connect(host='127.0.0.1',user='root',password='2002',database='speech_recognition',charset='utf8mb4'
,cursorclass=pymysql.cursors.DictCursor)



#conerting input string to list
user_input_list=user_input.split()

#creating a cursor object
cursorObject=connectionObject.cursor()

#creating list after removing inappropriate words
for my_val in user_input_list:
    if my_val not in invalid_words:
        insplit.append(my_val)
#print(insplit)
#converting list to string
insplit_str=' '.join(insplit)

if(insplit_str.startswith('make') | insplit_str.startswith('create')):
    print("First if")
    if('directory' in insplit_str):
        print("Second if")
        path=insplit_str.split()
        len=len(path)
        print("Hello")
        mylist=[]
        if('create' in path & 'directory' in path):
            path.remove('create')
            path.remove('directory')
        elif('create' in path & 'folder' in path):
            path.remove('create')
            path.remove('folder')
        elif('make' in path & 'folder' in path):
            path.remove('make')
            path.remove('folder')
        elif('make' in path & 'directory' in path):
            path.remove('make')
            path.remove('directory')
        print(path)
        str='/'.join(path)
        command="mkdir /"+str
        print(command)
        os.system(command)
        # print(path)
        # home_path=path[2]
        # user_path=path[3]
        # desk=path[4]
        # directory=path[5]
        # command="mkdir"+" /"+home_path+"/"+user_path+"/"+desk+"/"+directory
        # print(command)
        # os.system(command)
#for calendar command
if(insplit_str.startswith('calender')):

    #calendar command with year
    if(len(insplit_str)>=9):
        year=insplit_str[9:]
        command="cal "+year
        os.system(command)
    else:
        #without year
        os.system('cal')
else:

    #SQL Query
    var='"'+insplit_str+'"'
    sqlQuery="select command from commands where user_input="+var
    #print(sqlQuery)

    #executing sql query
    cursorObject.execute(sqlQuery)

    #fetching data from sql
    rows=cursorObject.fetchall()
    dict=rows[0]
    val=list(dict.values())
    inp=val[0]
    os.system(inp)
    s=''.join(val)

# except Exception as e:
#     #Exception Caught
#     print("Exception Occured")
# #
# finally:
    #CLosing the connection
    connectionObject.close()
