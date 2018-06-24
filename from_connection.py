import sys
import json

title = sys.argv[1]
author = sys.argv[2]
content = sys.argv[3]
out = json.loads(content.replace("'", '"'))

create_obj = {}


filelist = "text.txt"
file = open(filelist,"w+")
file.write(title)
file.write(author)
file.close()


from StartFromConnection import starttheprocessremotely
starttheprocessremotely(author,title,out)



