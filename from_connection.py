import sys
from configparser import ConfigParser
import pymysql
import json

config = ConfigParser()
config.read('config.ini')

HostName = config.get('database','HostName')
DatabaseName = config.get('database','DatabaseName')
HostUser = config.get('database','HostUser')
HostPass = config.get('database','HostPass')

db = pymysql.connect(HostName,HostUser,HostPass,DatabaseName, charset='utf8')

title = sys.argv[1]
author = sys.argv[2]
content = sys.argv[3]
out = json.loads(content.replace("'", '"'))

location = "newtext.txt"

file = open(location, "w+")
for listitem in out:
    from StartFromConnection import start_the_process
    file.write("\n")
    file.write("Typeof full-list (multiple lists): " + str(type(out)))
    file.write("\n")
    file.write("Typeof full-list (multiple lists): " + str(type(listitem)))
    file.write("\n")
    file.write("Typeof full-list (multiple lists): " + listitem[2])
    file.write("\n")

file.close()
start_the_process(listitem, db)

db.close()



