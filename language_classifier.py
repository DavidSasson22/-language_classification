import os
from ngrams import compute_ngrams_frequency


def build_language_model(language1_filename, language2_filename, k):
    """this function takes two file names as parameter, and return a list
    of dictionaries for each file. it acts like 'compute_ngrams_frequency'
    but takes a file as parameter, rather than a string"""
    if os.path.isfile(language1_filename) and os.path.isfile(language2_filename):
        with open(language1_filename) as file:
            reader = file.read()
            reader = reader.replace('\n', "")
            language1_dict = compute_ngrams_frequency(reader, k)
        with open(language2_filename) as file:
            reader = file.read()
            reader = reader.replace('\n', "")
            language2_dict = compute_ngrams_frequency(reader, k)
            if language1_dict == {} or language2_dict == {}:
                return None
        return language1_dict, language2_dict
    else:
        return None


def compute_ngram_distance(dict1, dict2):
    """this function takes two dicts as parameter, and calculates the total gap between
    them (it calculates the difference between each identical keys in the dictionaries)"""
    result = {}
    final_result = 0
    for key, value in dict1.items():
        if key in dict2:
            result[key] = abs(value - dict2[key])
        else:
            result[key] = value
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
    for key, value in result.items():
        final_result += value
    return final_result


def from_txt_to_ngrams(text_file, n):
    """this function acts like 'compute_ngrams_frequency'
    but takes a file as parameter, rather than a string"""
    with open(text_file) as file:
        reader = file.read()
        reader = reader.replace('\n', "")
    return compute_ngrams_frequency(reader, n)


def compute_relative_distance(source, dict1, dict2):
    """this function calculate the relative distance between two dictionaries
    and one txt source. as the distance is smaller, the chances are that the source
     and the dictionary share the same language"""
    dist1 = compute_ngram_distance(source, dict1)
    dist2 = compute_ngram_distance(source, dict2)
    relative_distance = dist1 / (dist1 + dist2)
    return relative_distance


def classify_language(text_to_classify, list_of_dicts1, list_of_dicts2, threshold):
    """this function determines whether a txt file is writen is one language
    or another, using relative distances and a threshold value"""
    if threshold > 0.5:
        print("ERROR: threshold > 0.5")
        return None
    k = 14
    classify_dicts = from_txt_to_ngrams(text_to_classify, k)
    n = 1
    while n < k:
        if classify_dicts[n] != {} and list_of_dicts1[n] != {} and list_of_dicts2[n] != {}:
            relative_distance = compute_relative_distance(classify_dicts[n], list_of_dicts1[n], list_of_dicts2[n])
            if relative_distance < threshold:
                return 1
            elif 1 - relative_distance < threshold:
                return 2
            else:
                n += 1
    return 0

