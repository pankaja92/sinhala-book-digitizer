

def getSuggestions(db):
    new_dict = {}
    try:
        with db.cursor() as cursor:
            sql_query = "SELECT word,permutation_suggestions,med_suggestions FROM temp_suggestions"
            cursor.execute(sql_query)
            get_val = cursor.fetchall()
            for suggestions_as_tuples in get_val:
                firstremoved = []
                suggestion = list(suggestions_as_tuples)
                full_suggestions = suggestion[1] + suggestion[2]
                full_suggestions_list = full_suggestions.split(",")
                full_suggestions_list.pop(0)
                new_dict[suggestion[0]] = full_suggestions_list
        cursor.close()
        return new_dict

    except Exception as inst:
        print(inst)
