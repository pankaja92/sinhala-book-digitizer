import json
import requests

url = "http://localhost:3000/senddata"

def return_json(data,id,author,title):
    a = {"content":data, "id":id, "author":author, "title":title}
    python2json = json.dumps(a, separators=(',', ':'))
    content = json.loads(python2json)
    response = requests.post(url, json=content)
    return response
