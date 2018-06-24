import itertools
from tokenize_words import tokenizer

tokens = [['p','ලෝක', 'ත්‍රස්තවාදයේ', 'ගොදුරු', 'බවට', 'පත්', 'ව', 'සින', 'ඕනෑ', 'ම', 'රාජ්‍යයක'], ['නායකයකු', 'සිය', 'කල්පනාව', 'දෙවරක්', 'යොමු'], ['කළයුතු', 'වැදගත්', 'අදහසක්', 'ශ්‍රී', 'ලංකාවේ', 'p']]


newlist = list(itertools.chain.from_iterable(tokens))


tokenizer(newlist)