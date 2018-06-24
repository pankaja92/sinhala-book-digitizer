import json
import requests

data = [['p','මේ' ,'කවියත්' ,'ගන' ,'ඇති', 'සැටයි','p'],['p', 'පණ්ඩුවාස', 'රජු' ,'ගේ', 'ඇවෑ', 'මෙන්', 'ඔහු', 'පුත්' ,'අභය','කුමාරයා', 'රජ', 'බව','p'],['p', 'ලංකාවේ', 'නියම', 'ඉතිහාසය', 'ආරම්භ', 'වන්නේ', 'ලංකාවාසීන්', 'බුදු', 'සමය', 'වැළදගත්']]
author = "My3pala Sira"
title= "dina 100"
id =  "001"

url = "http://localhost:3000/getdata"


def return_json(data):
    a = {"words":data, "id":id, "author":author, "book":title}
    python2json = json.dumps(a)
    filters = json.loads(python2json)
    return filters


def sendjson(jsondata):
    response = requests.post(url, json=jsondata)
    return response

jsondata = return_json(data)
# print(jsondata)
sendjson(jsondata)