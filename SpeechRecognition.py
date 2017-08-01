import speech_recognition as sr
from nltk.tokenize import word_tokenize
import time
import os
import json
import mysql.connector as mc
import info                                       #importing the self created package- info 

# making a dictionary of available databases
# creating dictionary ,the values are based on, how many ways python interpreter recognises your speech

db_available={'meetups':['meetups','meetup','meet up'],'mysql':['mysql','my SQL','Mysql'],
              'performance_schema':['performance','performance schema','performance Schema'],
              'pythondb':['Python DB','pythonDb','pythondb'],'sakila':['shakila','Shakeela','sakila'],
              'sys':['sis','fish','sys'],'world':['word','world','Word']}
dbkeys=db_available.keys()      # listing keys of db_available


# asking for task to do ,i said - make connection to MySQL Server

r = sr.Recognizer()
with sr.Microphone() as source:
    print("What can i do for you?")
    audio = r.listen(source)
spoken = r.recognize_google(audio)
spoken_tokenize=word_tokenize(spoken)
for i in spoken_tokenize:
    if(i=="connect" or i=="connection"):
        print ("I heard You, please wait while we connect you to MySql Server.")
        time.sleep(3)
        print("Now you are connected to MySql Server")
        time.sleep(3)
print ("\nBefore making connection to any particular database,you have to choose one of the available databases \n")
time.sleep(4)

# listing down the available databases on MYSQL Server
bList = os.walk("C://ProgramData//MySQL//MySQL Server 5.7//Data").next()[1]   #for listing only directories not files
for dt in bList:
    print dt


while True:
    if spoken== 'exit':                                          #terminating from MYSQL Server
        time.sleep(3)
        print "Connections are terminated !"
        break



    try:

        r = sr.Recognizer()                                      #recognizing what you say such as any command
        with sr.Microphone() as source:

             print("\nSay Now !")
             audio = r.listen(source)
        spoken = r.recognize_google(audio)

        for j in range(0, 7):
            for k in range(0, 3):
                if (spoken == db_available[dbkeys[j]][k]):                       #connecting to desired database you chose
                        keyMark=dbkeys[j]
                        print "please wait while we connect you to  "+keyMark+" database"
                        time.sleep(3)
                        print "Enter your Credentials"
                        time.sleep(3)
                        username=raw_input("Enter Your Username")                #asking for your username and password
                        time.sleep(2)
                        password=raw_input("Enter Your Password")
                        db = mc.connect(user=username, password=password,
                                        host='127.0.0.1',
                                        database=keyMark)
                        print "Please Wait while we connect you to desired database ..."
                        time.sleep(3)
                        print "You are connected to "+keyMark +" database"
                        time.sleep(3)
                        print "These are the tables stored in this database"
                        cursor = db.cursor()
                        sql = "show tables;"
                        cursor.execute(sql)
                        result = cursor.fetchall()                  #fetching all available tables in your chosen database
                        print json.dumps(result)                   # showing tables in json format

        sen_token = word_tokenize(spoken)                    #tokenizing  your command
        word_list = [x.encode('UTF8') for x in sen_token]    #removing unicodes from your tokenized command
        if("add" in word_list or "insert" in word_list):
            insert_query=info.entryIn(spoken)                #calling entryIn() from info package
            cursor.execute(insert_query)
            db.commit()
            print "record Inserted Successfully !"

        else:
            sql_query=info.keywords(spoken.lower(),word_list)   #calling keywords() from info package if "insert" is not found
            final_query=word_tokenize(sql_query)
            for kw in final_query:
                if(kw=="select"):                                #select command block
                    cursor.execute(sql_query)
                    query_result = cursor.fetchall()
                    for record in query_result:                  # you can use json.dumps() here for getting result in json
                        print record
                if (kw == "delete"):                            # delete command block
                    cursor.execute(sql_query)
                    db.commit()
                    print "records deleted !"
                if (kw == "update"):                           # update command block
                    cursor.execute(sql_query)
                    db.commit()
                    print "records updated successfully"
                if (kw == "exit"):                            # exiting from your current database
                    db.close()
                    print "connection is being terminated,please wait for a moment!"
                    time.sleep(4)
                    print "Now,you are no longer connected to any of databases"
                    break









    except sr.UnknownValueError:                                           #exceptions handled here
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


