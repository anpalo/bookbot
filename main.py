from operator import itemgetter


def get_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    letters = []
    for letter in text.lower():
        letters.append(letter)
    count_letter_list = []
    char_freq = {}
    for char in letters:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for key, value in char_freq.items():
        if key.isalpha():
            new_tuple = (key, value)
            count_letter_list.append(new_tuple)
    return count_letter_list


def get_sorted_list(some_list):
    sorted_list = sorted(some_list, key=itemgetter(1), reverse=True)
    return sorted_list


def get_report(text_name):
    print(f"---- Begin report of {text_name} ----\n {get_words(contents)} words found in the document\n")
    for item in get_sorted_list(count_char(contents)):
        if item[1] > 1:
            print(f"The {item[0]} character was found {item[1]} times")
        else:
            print(f"The {item[0]} character was found {item[1]} time")
    print("---- End report ----")


with open("books/frankenstein.txt") as f:
    contents = f.read()

get_report("books/frankenstein.txt")

