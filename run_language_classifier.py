import os
from language_classifier import build_language_model
from language_classifier import classify_language
from ngrams import write_list_of_ngram_dicts


def train_language_model():
    """this function takes from the user two txt file_names,
    and returns 2 dictionaries files, one for each txt"""
    language1 = input("Please enter the filename for language 1: ")
    language2 = input("Please enter the filename for language 2: ")
    ngram_max = input("Please enter the maximal length of the n-gram: ")
    language1_dicts, language2_dicts = build_language_model(language1, language2, int(ngram_max))
    write_list_of_ngram_dicts(language1_dicts, language1.replace(".txt", ".dict"))
    write_list_of_ngram_dicts(language2_dicts, language2.replace(".txt", ".dict"))


def classify_unknown_text():
    """this functions takes from the user 2 txt files, writen in two different languages
    and one file written in an unknown language. the function determine if the unknown txt
    file is writen in the same language as one of the other txt files"""
    condition = False
    while condition is False:
        language1 = input("Please enter the filename for language 1: ")
        language2 = input("Please enter the filename for language 2: ")
        filename = input("Please enter the filename to classify: ")
        if filename == "exit":
            return None
        if os.path.isfile(language1) and os.path.isfile(language2) and os.path.isfile(filename):
            condition = True
        if condition is False:
            print("File error: some files do not exist")
        else:
            ngram_max = input("Please enter the maximal length of the n-gram: ")
            threshold = input("Please enter threshold value between 0 and 0.5: ")
            language1_dicts, language2_dicts = build_language_model(language1, language2, int(ngram_max))
            result = (classify_language(filename, language1_dicts, language2_dicts, float(threshold)))
            if result == 1:
                print("I believe the text matches the language in {}".format(language1))
            elif result == 2:
                print("I believe the text matches the language in {}".format(language2))
            else:
                print("Sorry, I could not figure this one out!")
                condition = False

