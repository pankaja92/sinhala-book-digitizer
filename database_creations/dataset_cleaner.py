from nltk import word_tokenize
import re
import os

root = '../resources/collection/'
write_location = '../resources/cleaned_set/'

def readFileByFile(root, write_location):
    path, dirs, files = os.walk(root).__next__()
    word_list = {}
    count = 0
    for file in files:
        filename = root + file
        openFile = open(filename, 'r', encoding='utf-16')
        text = openFile.read()
        tokenized_set = word_tokenize(text)

        regex = re.compile(r'\b[A-Z]{1,}\b')
        filtered = list(filter(lambda i: not regex.search(i), tokenized_set))
        print(filtered)
        print(filtered.__len__())

        regex_1 = re.compile(r'<|>|,|[0-1]')
        filtered1 = list(filter(lambda i: not regex_1.search(i), filtered))
        print(filtered1)
        print(filtered1.__len__())

        f = open((write_location + filtered),"w+",encoding='utf-16')
        f.write(filtered)
        f.close()


readFileByFile(root, write_location)
