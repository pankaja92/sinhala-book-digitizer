from itertools import  product

# top rank
constants = {
    'ක':['ඛ'], 'ඛ':['ක'], 'ථ':['ත'], 'ත':['ථ'], 'ග':['ඝ'], 'ඝ':['ග'],
    'ඣ':['ජ'], 'ජ': ['ඣ'], 'ප':['ඵ'], 'ඵ':['ප'], 'ච': ['ඡ'], 'ඡ':['ච'],
    'ඨ': ['ට'], 'ට':['ඨ'], 'ණ':['න'], 'න':['ණ'], 'ද':['ධ'], 'ධ':['ද'],
    'භ':['බ'], 'බ':['භ']
}


def constants_permutations(word):
    # create list of list of letters
    list_of_letters = [[letter] + constants[letter] if letter in constants else [letter] for letter in word]
    all_permutations = product(*list_of_letters)  # get all permutations
    joined_words = list(map(''.join, all_permutations))  # join letters in to a string
    return joined_words


constants_permutation_dictionary = {}


def topPermutations(misspelled_list, db):
    from suffix_spellchecker import suffixspellchecker
    for word in misspelled_list:
        constantslist = constants_permutations(word)
        constants_permutation_dictionary[word] = constantslist
    suffixspellchecker(constants_permutation_dictionary, db)