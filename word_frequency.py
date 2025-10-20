#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    sentence = input("enter a sentence: ")
    while not is_sentence(sentence):
        print("this doesnt meet the criteria for a sentence")
        sentence = input("enter a sentence: ")
    return sentence


def calculate_frequencies(sentence):
    words = sentence.split()
    unique_words = []
    frequencies = []

    for word in words:
        word = word.strip(".,!?").lower()
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)

    return unique_words, frequencies

def print_frequencies(words, frequencies):
    print("Word Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


main()
