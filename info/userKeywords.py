import re
from nltk import word_tokenize
def keywords(kry,getlist=[]):
    # creating list of your values by indentifying those in between @ [example - remove records of registration table where id ie equal to @ 2 @ ]
    field_list = re.findall(r'\@([^@]*)\@', kry)

   #dictionary for keywords those you may speak,the values are based on how your python interpreter recognises your speech

    query_dict = {'select': ['display', 'list', 'give', 'get', 'show', 'fetch', 'select'],
                  '*': ['all', '', '', '', '', '', ''],'from': ['from', 'of', '', '', '', '', ''],

                  'user': ['user', '', '', '', '', '', ''],'registration': ['registration', '', '', '', '', '', ''],

                  'delete':['delete','remove','vanish','','','',''],'where':['where','were','','','','',''],
                  '=':['is','is equalto','is equal to','isequal to','isequalto','',''],

                  'update':['update','make','','','','',''],'set':['set','sat','edit','replace','','',''],
                  'id': ['id', 'ID', '', '', '', '', ''],'date': ['date', 'data','Date','DATE','','',''],
                  'description': ['description', 'Description','DESCRIPTION','','','',''],'end':['end','and','END','AND','End','And',''],
                  'guest':['guest','just','Guest','GUEST','','',''],'presenter':['presenter','presenters','Presenter','PRESENTER','','',''],
                  'start':['start','Start','START','','','',''],'title':['title','Title','TITLE','','','',''],

                  'exit':['exit','quit','exist','terminate','','',''],'connection':['connections','connection','','','','','']
                    }

    a=0

    query_keys = query_dict.keys()
    query_list=[]





    for words in getlist:                               #checking your spoken statement to dictionary and creating desirable sql query
        for i in range(0,20):
            for j in range(0,7):
                if (words == query_dict[query_keys[i]][j]):
                    query_list.append(query_keys[i])
                    if (query_keys[i] == '='):
                        query_list.append('"')
                        query_list.append(field_list[a])
                        query_list.append('"')
                        a+=1

    sql_query = ' '.join(query_list)                        #joining all values to make one sql query
    return sql_query



