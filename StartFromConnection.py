
def start_the_process(tokenized_words,db):
    from checkSpellings import spellChecker
    from get_suggestions_from_db import getSuggestions

    spellChecker(tokenized_words,db)
    get_suggestions = getSuggestions(db)
    print(get_suggestions)
    db.close()

