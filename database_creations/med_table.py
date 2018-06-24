from nltk import word_tokenize
import pymysql

# ලද්දේ
import operator
# from configparser import  ConfigParser
#
# config = ConfigParser()
# config.read('config.ini')
#
# HostName = config.get('database','HostName')
# DatabaseName = config.get('database','DatabaseName')
# HostUser = config.get('database','HostUser')
# HostPass = config.get('database','HostPass')

db = pymysql.connect("localhost","pankaja","Ilovenc.tp1","pankaja", charset='utf8')

file = '../resources/collection/custom1.txt'
text_file = open("Output.txt", "w")
open_file = open(file,'r',encoding='utf-8')

readFile = open_file.read()
# st = 'Carry out a random act of kindness, with no expectation of reward, safe in the knowledge that one day someone might do the same for you'

tokenized_list = word_tokenize(readFile)

tokenized_set = set(tokenized_list)

sorted = sorted(tokenized_set)
# text_file.write(','.join(map(str, sorted)) )
# text_file.close()

print(tokenized_set)

try:
    with db.cursor() as cursor:
        for word in tokenized_set:
            word_length = word.__len__()
            print(type(word_length))
            if(word == '\ufeff'):
                continue
            # Create a new record
            else:
                SQL_Query = "INSERT INTO `Minimum_Edit_Distance` (`word`,`word_length`) VALUES (%s,%s)"
                cursor.execute(SQL_Query,(word,word_length))
                db.commit()
            word_length = 0

finally:
    db.close()


#
