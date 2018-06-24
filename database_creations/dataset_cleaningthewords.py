from nltk import word_tokenize
import os
import re

def readFileByFile(root):
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

        regex_1 = re.compile(r'<|>|,|[0-1]')
        filtered1 = list(filter(lambda i: not regex_1.search(i), filtered))
        print(file)
        unique_set = set(filtered1)
        for word in unique_set:
            count = filtered1.count(word)
            word_list[word] = count
            count = 0

    return word_list
