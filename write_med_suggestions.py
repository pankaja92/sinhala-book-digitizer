
def write_to_med_list(word,suggest_list,db):
    try:
        newString = ''
        for suggest_word in suggest_list:
            if newString == '':
                newString = suggest_word
            else:
                newString = newString + ',' + suggest_word
        with db.cursor() as cursor:
            sql_query_insert = "UPDATE temp_suggestions SET med_suggestions=%s WHERE word=%s"
            print(newString)
            print(word)
            cursor.execute(sql_query_insert, (newString, word))
            db.commit()
        cursor.close()
    except Exception as inst:
        print(inst)