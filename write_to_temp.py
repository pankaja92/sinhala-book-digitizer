
def write_to_temp(incorrect_words_list, db):
    try:
        with db.cursor() as cursor:
            for word in incorrect_words_list:
                sql_query = "SELECT id FROM temp_suggestions WHERE word= %s"
                new_val = cursor.execute(sql_query, word)
                if new_val != 1:
                    sql_query_insert = 'INSERT INTO `temp_suggestions` (`word`) VALUES (%s)'
                    cursor.execute(sql_query_insert,word)
                    db.commit()
        cursor.close()
    except Exception as inst:
        print(inst)

