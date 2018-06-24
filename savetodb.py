

def savelocation(author,bookname,fullstring,db):
    print("Author : " + author)
    try:
        with db.cursor() as cursor:
            sql_query = "INSERT INTO book_content (author, title, content) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (author, bookname, fullstring))
            cursor.fetchone()
            db.commit()
            sql_query_get= "SELECT id FROM book_content WHERE title=(%s)"
            cursor.execute(sql_query_get,bookname)
            get_new_val = cursor.fetchone()
            id = get_new_val[0]
        cursor.close()
        return id

    except Exception as inst:
        print(inst)