suffixes = ['වලට','වල','යේ','යට','ගේ','ක්','ිමින්','මින්']

new_dict = {}

# Add prefixes if no prefixes is added into the word


def addSuffixes(misspelled_list, db):
    from suffix_spellchecker import suffixspellchecker
    for misspelled_word in misspelled_list:
        suffix_in = False
        word_list = []
        for suffix in suffixes:
            if(misspelled_word.endswith(suffix)):
                suffix_in = True
                continue
            else:
                word = misspelled_word + suffix
                word_list.append(word)
        if suffix_in==False:
            new_dict[misspelled_word] = word_list
    suffixspellchecker(new_dict, db)
