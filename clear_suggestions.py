
def cleartempsuggestions(db):
    try:
        with db.cursor() as cursor:
            delete = "DELETE FROM temp_suggestions"
            cursor.execute(delete)
        cursor.close()
        db.commit()
    except Exception as inst:
        print(inst)