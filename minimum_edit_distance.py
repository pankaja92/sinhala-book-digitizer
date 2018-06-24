

def sort_in_med(db):
    from minimum_edit_distance_list import create_words_list
    from read_suggestions import readsuggestions
    from levenshtein_distance import minimum_edit_distance
    from write_med_suggestions import write_to_med_list
    miss_list = readsuggestions(db)
    med_words_dict = create_words_list(db)
    for miss_word in miss_list:
        miss_length = len(miss_word)
        dict_for_miss_word = {}
        words_list = []
        for other_length in range((miss_length-1),(miss_length+1)):
            dictionary_words_list = med_words_dict.get(other_length)
            if dictionary_words_list is not None:
                for dictionary_word in dictionary_words_list:
                    med = minimum_edit_distance(miss_word,dictionary_word)
                    dict_for_miss_word[med] = dict_for_miss_word.get(med, [])
                    dict_for_miss_word[med].append(dictionary_word)

        sorted_dict = sorted(dict_for_miss_word.items())
        new_list = []
        for newtuple in sorted_dict:
            new_list = new_list + newtuple[1]

        anotherlist = new_list[:12]
        write_to_med_list(miss_word,anotherlist,db)
