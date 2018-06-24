import nltk
import collections
import pymysql


location1 = '../resources/cleaned_set/100.txt'
f1 = open(location1,'r',encoding='utf-16')
raw1 = f1.read()

location2 = '../resources/cleaned_set/text.txt'
f2 = open(location2,'r')
raw2 = f2.read()

tokens = nltk.word_tokenize(raw1)
tokens2 = nltk.word_tokenize(raw2)

#Create your bigrams
bgs1 = nltk.bigrams(tokens)
bgs2 = nltk.bigrams(tokens2)


d = {}
#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs1)
fdist2 = nltk.FreqDist(bgs2)

for k,v in fdist.items():
    d[v] = d.get(v, [])
    d[v].append(k)


od = collections.OrderedDict(sorted(d.items(), reverse=True))

# print(od)
# the_list = dict(od)
# print(od)
# # for tupel_item in od:
# #     print(tupel_item)
#
#
# the_list = ([(333, [('a', 'b'), ('a', 'b')]), (96, [('x', 'y'), ('x', 'y')]), (88, [('abc', 'xy'), ('abc', 'xy')]),(12, [('pgr', 'grq'), ('abd', 'dba'), ('za', 'az')])])
#
# print(the_list)
# the_list = dict(the_list)

# print(the_list)

db = pymysql.connect('localhost','pankaja','Ilovenc.tp1','pankaja', charset='utf8')

the_list = dict(od)

try:
    with db.cursor() as cursor:
        # for word in incorrect_words_list:
        #     sql_query = 'INSERT INTO `temp_suggestions` (`word`) VALUES (%s)'
        #     cursor.execute(sql_query, word)
        #     db.commit()
        for key, val in the_list.items():
            for j, k in val:
                print(str(key) + ' : ' + j + ' ' + k)
                sql_query = "INSERT INTO bigram_frequencies (first_word,second_word,frequency) VALUES (%s, %s, %s)"
                cursor.execute(sql_query,(j,k,key))
                db.commit()
    cursor.close()
except Exception as inst:
    print(inst)

db.close()