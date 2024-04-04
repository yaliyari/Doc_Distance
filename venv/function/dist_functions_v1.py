import os
import sys
import pandas as pd
import numpy as np
import math

method = 3
# function to read the input text filesP
def read_text_files(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except IOError:
        print(f"An IOError occurred while attempting to read  {file_name}!")
        sys.exit()


def get_words_from_list(line_list):
    """parse the list lines from the previous method, into words
    and return list of words"""
    word_list = []
    print(method)
    for line in line_list:
        word_in_line = get_word_from_string(line)

        if method == 1:
            word_list = word_list + word_in_line   # word_in_line itself is a list of words crated from a line
            # This is the bottleneck, since "+" requires O(l1+l2), in contrast to extend method that is O(l2)
            # the complexity of "+" is O(W^2/k), where k is length of a line, and W is the total number of words
            # in the first iteration it adds list of length k, the second iteration requires k+k, the third one would be
            # 2k+k, and so on...
        else:
            word_list.extend(word_in_line)
            # extend method reduces the complexity, since it only requires tetha(m) to add list of length m to the
            # current list. Then it is repeated W/k times, so O(W/k x m) say m=k worst case, then O(W)

    return word_list


def get_word_from_string(line):
    """receive a line from the file and returns a list of words in the line
    the complexity of this function is O(N), N is the length of the line, assuming each word has length W"""
    word_list = []
    character_list = []
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)   # to move the list of characters into a string
            word = word.lower()
            word_list.append(word)
            character_list = []
    # for the last character list
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list


def word_frequency_count(word_list):
    """return a list of pair in format of (word, frequency)
    the complextity is O(W xL), where W is the total number of words in the doc and L is the number of unique
    words"""
    pair_list = []
    for new_word in word_list:
        for prev_words in pair_list:
            if new_word == prev_words[0]:
                prev_words[1] += 1
                break
        else:
            pair_list.append([new_word, 1])  # if break then the word already exists and just we added to frequency
    if method == 3:
        insertion_sort(pair_list)
    return pair_list


def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


def inner_product(l1, l2):
    """ to calculate the inner production between frequency of words in two vectors
    each item in a vector has the form of (word,freq)"""
    sum_inner = 0
    for word1, freq1 in l1:
        for word2, freq2 in l2:
            if word1 == word2:
                sum_inner += freq1 * freq2
    return sum_inner


def calc_angle(l1, l2):
    """ to calculate the angle between two vectors, using the inner product method"""
    numerator = inner_product(l1, l2)
    norm_l1 = inner_product(l1, l1)
    norm_l2 = inner_product(l2, l2)
    denominator = math.sqrt(norm_l1 * norm_l2)
    return math.acos(numerator/denominator)
