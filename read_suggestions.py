

def readsuggestions(db):
    new_dict = []
    try:
        with db.cursor() as cursor:
            sql_query = "SELECT word,permutation_suggestions FROM temp_suggestions"
            cursor.execute(sql_query)
            get_val = cursor.fetchall()
            for suggestions_as_tuples in get_val:
                suggestion = list(suggestions_as_tuples)
                new_dict.append(suggestion[0])
        cursor.close()
        return new_dict

    except Exception as inst:
        print(inst)

