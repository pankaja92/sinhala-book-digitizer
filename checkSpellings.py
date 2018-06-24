

incorrect_words_list = []

def spellChecker(tokenized_text,db):
    try:
        with db.cursor() as cursor:
            for word in tokenized_text:
                SQL_Query = "SELECT * FROM corpus WHERE word= %s"
                val = cursor.execute(SQL_Query, word)
                if val != 1:
                    incorrect_words_list.append(word)
        cursor.close()
        from write_to_temp import write_to_temp
        from general_suffixes import addSuffixes
        from permutationchecker import mainPermutations
        from constant_permutations import topPermutations
        from minimum_edit_distance import sort_in_med
        write_to_temp(incorrect_words_list, db)
        addSuffixes(incorrect_words_list, db)
        topPermutations(incorrect_words_list, db)
        mainPermutations(incorrect_words_list, db)
        sort_in_med(db)
    except Exception as inst:
        print(inst)

