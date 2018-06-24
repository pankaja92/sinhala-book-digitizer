import pymysql
import operator
from configparser import  ConfigParser
from database_creations.dataset_cleaningthewords import readFileByFile

config = ConfigParser()
config.read('./config.ini')

HostName = config.get('database','HostName')
DatabaseName = config.get('database','DatabaseName')
HostUser = config.get('database','HostUser')
HostPass = config.get('database','HostPass')

db = pymysql.connect(HostName,HostUser,HostPass,DatabaseName, charset='utf8')

root = '../resources/collection/'

get_word_list = readFileByFile(root)

try:

    with db.cursor() as cursor:
        sorted_word_list = sorted(get_word_list.items(), key=operator.itemgetter(1), reverse=True)
        for obj in sorted_word_list:
            # Create a new record
            print("Query executing started")
            SQL_Query = 'INSERT INTO `test` (`word`, `count`) VALUES ("%s", "%s")' % (obj[0], obj[1])
            cursor.execute(SQL_Query)
            db.commit()


finally:
    db.close()
