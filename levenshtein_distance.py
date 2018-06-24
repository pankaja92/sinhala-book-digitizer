

def minimum_edit_distance(misspelled_word, dictionary_word):
    if len(misspelled_word) > len(dictionary_word):
        misspelled_word, dictionary_word = dictionary_word, misspelled_word

    distances = range(len(misspelled_word) + 1)
    for counter_1, value_1 in enumerate(dictionary_word):
        distances_ = [counter_1+1]
        for counter_2, value_2 in enumerate(misspelled_word):
            if value_2 == value_1:
                distances_.append(distances[counter_2])
            else:
                distances_.append(1 + min((distances[counter_2], distances[counter_2 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
