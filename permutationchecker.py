from itertools import  product
from general_spell_checker import generalspellchecker

# second rank
diacritics_permutation_list = {
    'ැ': ['ෑ', 'ා', 'ෘ'], 'ෑ': ['ැ', 'ා', 'ෘ'], 'ා': ['ෑ', 'ැ', 'ෘ'], 'ෘ': ['ෑ', 'ැ', 'ා'],
    'ී' :['ි'], 'ි': ['ී']
}

# third rank
permutation_list = \
    {
        'ක': ['ත','හ','ග','භ','න','ශ'], 'ත': ['ක','හ','ග','භ','න','ශ'],
        'හ': ['ක','ත','ග','භ','න','ශ'], 'ග': ['ක','ත','හ','භ','න','ශ'],
        'භ': ['ක','ත','හ','ග','න','ශ'], 'න': ['ක','ත','හ','ග','භ','ශ','ණ'],
        'ල': ['ළ'], 'ළ': ['ල'], 'ෂ': ['ස', 'ශ','ය','ස','ඝ','ජ','ඡ'],
        'ශ': ['ක','ත','හ','ග','භ','න','ස','ෂ'], 'ම': ['ව','ච','ධ','ඨ','බ','ට','ඛ','ඩ','ඪ'],
        'ට': ['ම','ච','ධ','ඨ','බ','ඛ','ඩ','ඪ','ඨ','ථ'],'ඤ': ['ඥ'], 'ඥ': ['ඤ'],
        'ව': ['ම','ච','ධ','ඨ','බ','ඛ','ඩ','ඪ','ට','ථ'], 'ච': ['ම','ට','ව','ධ','ඨ','බ','ඛ','ඩ','ඪ','ඡ'],
        'ධ': ['ම','ව','ච','ඨ','බ','ඛ','ඩ','ඪ','ට','ඵ'], 'ඨ': ['ට','ම','ව','ච','ධ','බ','ඛ','ඩ','ඪ','ඵ','ථ'],
        'බ': ['ම','ව','ච','ධ','ඨ','ඛ','ඩ','ඪ','ඵ'], 'ඛ': ['ම','ව','ච','ධ','ඨ','බ','ඩ','ඪ'],
        'ඩ': ['ම','ව','ච','ධ','ඨ','බ','ඛ','ඪ','ඵ'], 'ඪ': ['ම','ව','ච','ධ','ඨ','බ','ඛ','ඩ','ඵ'],
        'ඵ': ['ප','ම','ව','ච','ධ','ඨ','බ','ඛ','ඪ','ඩ'],
        'ය': ['ස','ඝ','ප','ජ','ඡ'],'ස': ['ය','ඝ','ප','ජ','ඡ','ශ','ෂ'],
        'ඝ': ['ය','ස','ප','ජ','ඡ'],'ප': ['ය','ස','ඝ','ජ','ඡ'],
        'ජ': ['ය','ස','ඝ','ප','ඡ','ඣ'],'ඡ': ['ය','ස','ඝ','ප','ජ','ච'],
        'අ': ['ද','උ','ඳ'], 'ද': ['අ','උ','ඳ'],
        'උ': ['අ','ද','ඳ'], 'ඳ': ['අ','ද','උ'],
        'ැ': ['ෑ', 'ා', 'ෘ'], 'ෑ': ['ැ', 'ා', 'ෘ'], 'ා': ['ෑ', 'ැ', 'ෘ'], 'ෘ': ['ෑ', 'ැ', 'ා'],
        'ී' :['ි'], 'ි': ['ී']
    }

permutation_dictionary = {}


def diacritics_permutations(word):
    # create list of list of letters
    list_of_letters = [[letter] + diacritics_permutation_list[letter] if letter in diacritics_permutation_list else [letter] for letter in word]
    all_permutations = product(*list_of_letters)  # get all permutations
    joined_words = list(map(''.join, all_permutations))  # join letters in to a string
    return joined_words


def letter_permutations(word):
    # create list of list of letters
    list_of_letters = [[letter] + permutation_list[letter] if letter in permutation_list else [letter] for letter in word]
    all_permutations = product(*list_of_letters)  # get all permutations
    joined_words = list(map(''.join, all_permutations))  # join letters in to a string
    return joined_words


def mainPermutations(misspelled_list, db):
    for word in misspelled_list:
        diacriticslist = diacritics_permutations(word)
        wordlist = letter_permutations(word)
        complete_list = diacriticslist + wordlist
        permutation_dictionary[word] = complete_list
    generalspellchecker(permutation_dictionary, db)
