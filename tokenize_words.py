from checkSpellings import spellChecker
from get_suggestions_from_db import getSuggestions


def tokenizer(tokenized_words,db):
    spellChecker(tokenized_words,db)
    get_suggestions = getSuggestions(db)
    return get_suggestions
