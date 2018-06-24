
SQL_QUERY = 'SELECT `length`,`word` FROM `corpus`'


def create_words_list(db):
    from collections import defaultdict
    try:
        with db.cursor() as cursor:
            cursor.execute(SQL_QUERY)
            data = cursor.fetchall()
            med_dataset = defaultdict(list)
            for  key, val in data:
                med_dataset[key].append(val)
            new_dict = dict(med_dataset)
        cursor.close()
        return new_dict
    except Exception as inst:
        print(inst)


