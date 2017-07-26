# this insertCmd.py is used for insert command only
import re
from nltk.tokenize import word_tokenize
import speech_recognition as sr
def entryIn(spoken):
    # creating dictionary ,the values are based on, how many ways python interpreter recognises your speech
    insert_dict={'insert into':['insert','add'],'registration values( ':['registration',''],'user values(':['user','']}

    insert_keys=insert_dict.keys()
    insert_list=[]



    lower_spoken=spoken.lower()    #converting your spoken command to lower case
    # print lower_spoken

    lower_spoken_tok=word_tokenize(lower_spoken)  # tokenizing
    field_list = re.findall(r'\@([^@]*)\@',lower_spoken)  # finding values in between @
    # print field_list
    length=len(field_list)





    for words in lower_spoken_tok:
        for m in range(0,3):
            for n in range(0, 2):
                if (words == insert_dict[insert_keys[m]][n]):
                    insert_list.append(insert_keys[m])

    for l in range(0,length):
        insert_list.append('"')
        insert_list.append(field_list[l])
        insert_list.append('"')
        if(l!=length-1):
            insert_list.append(',')
        else:
            insert_list.append(')')



    insert_query = ' '.join(insert_list)
    return insert_query



