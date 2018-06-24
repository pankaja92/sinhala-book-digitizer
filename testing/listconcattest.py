import itertools
from tokenize_words import tokenizer
newlist = [['p','ලෝක', 'ත්‍රස්තවාදයේ', 'ගොදුරු', 'බවට', 'පත්', 'ව', 'සින', 'ඕනෑ', 'ම', 'රාජ්‍යයක'], ['නායකයකු', 'සිය', 'කල්පනාව', 'දෙවරක්', 'යොමු'], ['කළයුතු', 'වැදගත්', 'අදහසක්', 'ශ්‍රී', 'ලංකාවේ', 'p']]


newlist1 = list(itertools.chain.from_iterable(newlist))

staart = True
def generate(newlist1):
    for idx, value in enumerate(newlist1):
        if value == 'p' and staart == True:
            newlist1[idx] = '<p>'
            staart != staart
        elif value == 'p' and staart == False:
            newlist1[idx] = '</p>'
            staart != staart
    print(newlist1)

#
generate(newlist1)