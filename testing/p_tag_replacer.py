import itertools

tokens = [['p','ලෝක', 'ත්‍රස්තවාදයේ', 'ගොදුරු', 'බවට'],['පත්', 'ව', 'සින', 'ඕනෑ', 'ම', 'රාජ්‍යයක','p'], ['p','නායකයකු', 'සිය', 'කල්පනාව', 'දෙවරක්', 'යොමු'], ['කළයුතු', 'වැදගත්', 'අදහසක්', 'ශ්‍රී', 'ලංකාවේ', 'p']]


newlist = list(itertools.chain.from_iterable(tokens))


beginning = True
for idx, value in enumerate(newlist):
    print(beginning)
    if value == 'p' and beginning == True:
        newlist[idx] = '<p>'
        beginning = not beginning
    elif value == 'p' and beginning == False:
        newlist[idx] = '</p>'
        beginning = not beginning
print(newlist)
