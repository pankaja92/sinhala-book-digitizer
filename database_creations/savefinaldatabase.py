import pymysql

db = pymysql.connect('localhost','pankaja','Ilovenc.tp1','pankaja', charset='utf8')

book = " <p> මේ කවියත් ගන ඇති සැටයි </p> <p> පණ්ඩුවාස රජු ගේ ඇවෑ මෙන් ඔහු පුත් අභය කුමාරයා රජ බව </p> <p> ලංකාවේ නියම ඉතිහාසය ආරම්භ වන්නේ ලංකාවාසීන් බුදු සමය වැළදගත් ලද්දේ දැයි මෙහි දී ප‍්‍රශ්නයක් නැහීය හැකි ය . ධර්මාශෝක රජු ගේ බලය ඉන්දියා අර්ධද්වීපයේ රජු සමගම් වැසියන් ගෙන් විශාල පිරිසක් ද බිද්ධාගම වැළද ගත්තෝ ය </p>"

def insertbookintodb(book):
    try:
        with db.cursor() as cursor:
            sql_query = 'INSERT INTO `book_content` (`content`) VALUES (%s)'
            cursor.execute(sql_query, book)
            db.commit()
        cursor.close()
    except Exception as inst:
        print(inst)

    db.close()


insertbookintodb(book)