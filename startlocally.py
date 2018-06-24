from tokenize_words import tokenizer
from savetodb import savelocation
from  send_data_final import return_json
from configparser import ConfigParser
import re
import pymysql
import itertools


config = ConfigParser()
config.read('config.ini')

HostName = config.get('database','HostName')
DatabaseName = config.get('database','DatabaseName')
HostUser = config.get('database','HostUser')
HostPass = config.get('database','HostPass')

db = pymysql.connect(HostName,HostUser,HostPass,DatabaseName, charset='utf8')

def starttheprocesslocally(obj):
    title = obj["title"]
    author = obj["author"]
    content = obj["content"]
    for line in content:
        getdata = tokenizer(line,db)
    print(getdata)
    concatantedList =list(itertools.chain.from_iterable(content))
    for n, i in enumerate(concatantedList):
        for key in getdata:
            if i == key:
                concatantedList[n] = getdata[key][0]
            elif i == 'P':
                concatantedList[n] = '<p>'
            elif i == 'NP':
                concatantedList[n] = '</p>'
            elif i == 'S':
                concatantedList[n] = '<h6>'
            elif i == 'NS':
                concatantedList[n] = '</h6>'
    fullbooktext = " ".join(concatantedList)
    getid = savelocation(author,title, fullbooktext,db)
    print(getid)
    # return_json(fullbooktext,getid,author,title)
    # displaystring = re.sub('<[^>]+>', '', fullbooktext)
    # startUI(displaystring,getdata)
    from clear_suggestions import cleartempsuggestions
    cleartempsuggestions(db)
    db.close()



object = {
    "title" : "Sinhala Ithihasaya",
    "author" : "Author Unknown",
    "content" : [['S','මේ' ,'කවියත්' ,'ගන' ,'ඇති', 'සැටයි','NS'],['P', 'නයම', 'ඉස', 'බුදු', 'සමය','P']]
}


completedlist = starttheprocesslocally(object)
