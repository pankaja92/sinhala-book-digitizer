
def suffixspellchecker(new_dict,db):
    with db.cursor() as cursor:
        for key, words_list in new_dict.items():
            for word in words_list:
                sql_query = "SELECT * FROM corpus WHERE word= %s"
                val = cursor.execute(sql_query,word)
                if val == 1:
                    # check suggestions if NULL or exists
                    sql_check_record = "SELECT permutation_suggestions FROM temp_suggestions WHERE word= %s"
                    cursor.execute(sql_check_record,key)
                    existing = cursor.fetchone()
                    val = existing[0]
                    # If NULL
                    if val == None:
                        sql_query_insert = "UPDATE temp_suggestions SET permutation_suggestions=%s WHERE word=%s"
                        cursor.execute(sql_query_insert,(key,key))
                        db.commit()
                    # If any value exists
                    else:
                        sql_get_exists = "SELECT permutation_suggestions FROM temp_suggestions WHERE word=%s"
                        cursor.execute(sql_get_exists, key)
                        get_val = cursor.fetchone()
                        existing_val = get_val[0]
                        if key not in existing_val:
                            update_val = existing_val + ','+key
                            update_query = "UPDATE temp_suggestions SET permutation_suggestions=%s WHERE word=%s"
                            cursor.execute(update_query, (update_val, key))
                            db.commit()
    cursor.close()

