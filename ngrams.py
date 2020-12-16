def remove_punctuation(txt1):
    """this function takes a string as parameter and return it without punctuation marks"""
    punctuation = "./:!?,;"
    stage1 = "".join(char for char in txt1 if char not in punctuation)
    result = stage1.replace("-", " ")
    return result


def split_lower_txt(txt2):
    """this function takes a string as parameter and return it as a list of low-letter words"""
    result = txt2.lower().split(" ")
    return result


def char_count(word_list, n):
    """this function takes a list of words as parameters, cuts each words to slices,
     and checks the frequency of each slice in the list"""

    result = []
    for word in word_list:
        i = 0
        while i + n <= len(word):
            new_slice = slice(i, i+n)
            chars = word[new_slice]
            result.append(chars)
            i += 1
    return result


def compute_ngram_frequency(txt3, n):
    """this function takes a string parameter,
    and returns a dictionary containing the frequency of each slice in the string"""
    result = {}
    stage1 = remove_punctuation(txt3)
    stage2 = split_lower_txt(stage1)
    stage3 = char_count(stage2, n)
    for sequence in stage3:
        result[sequence] = stage3.count(sequence)
    if "" in result:
        del result[""]
    total_value = sum(result.values())
    for key, value in result.items():
        result[key] = value/total_value
    return result


def compute_ngrams_frequency(txt4, k):
    """this function acts like the 'compute_ngram_frequency',
    but returns a list of dictionaries: each dictionary for different slice size"""
    result = []
    for i in range(1, k+1):
        stage1 = compute_ngram_frequency(txt4, i)
        result.append(stage1)
    return result


def ngram_dict_to_string(ngram_dict):
    """this function takes a dictionary similar to the 'compute_ngram_frequency' output,
     and returns it as a string"""
    result = "".join(i for i in str(ngram_dict) if i not in "}{'][ ").replace(",", " ")
    return result


def string_to_ngram_dict(str_dict):
    result = {}
    stage1 = str_dict.split(" ")
    for element in stage1:
        split_element = element.split(":")
        result[split_element[0]] = float(split_element[1])
    return result


def write_list_of_ngram_dicts(list_of_dicts, filename):
    """this function takes the 'compute_ngrams_frequency' out put and write it as a file"""
    with open(filename, "w") as file1:
        for dictionary in list_of_dicts:
            file1.write(ngram_dict_to_string(dictionary))
            file1.write("\n")


def load_list_of_ngram_dicts(input_file):
    """this function takes the output file of 'write_list_of_ngram_dicts',
    reverse its process, and returns a list of dictionaries """
    stage3 = []
    stage4 = []
    with open(input_file, "r") as file:
        stage1 = file.read().split("\n")
        stage1.remove("")
    for element in stage1:
        stage2 = element.split(" ")
        stage3.append(stage2)
    dict_len = len(stage3)
    for i in range(0, dict_len):
        new_dict = {}
        for element in stage3[i]:
            key_value = element.split(":")
            new_dict[key_value[0]] = float(key_value[1])
        stage4.append(new_dict)
        new_dict = {}
    return stage4

