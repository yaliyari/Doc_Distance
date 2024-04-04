#!/usr/bin/env
"""
Finding document distance,
Exercise from Introduction to Algorithm course
https://courses.csail.mit.edu/6.006/fall11/index.shtml

website to get books in text files to test: https://www.gutenberg.org/
The goal is to compute the distance between two text files, measured by the angle between their word frequency vectors
For complexity analyses, assume Z lines in a document, each line has length N words, and each word includes w characters
 (i.e., #of words in
in line N/(w+1) and the number of words in a document would be W = Z * k
"""
import sys

from function import dist_functions_v1
import numpy as np
import os


def main():
    os.chdir("./input_date/")
    print("Hi")

    # If you run the code using Pycharm or other IDEs
    text_files = ['Gatsby.txt', 'MobyDick.txt', 'Picture_Gray.txt', 'Tale_2Cities.txt', 'test1.txt', 'test2.txt']
    if len(sys.argv) != 3:
        print("set the file names inside the code")
        f_name1 = text_files[0]
        f_name2 = text_files[0]
    else:
        # If you run the code from the command line format: main_simple.py filename_1 filename_2
        f_name1 = sys.argv[1]
        f_name2 = sys.argv[2]

    f_data1 = dist_functions_v1.read_text_files(f_name1)
    f_data2 = dist_functions_v1.read_text_files(f_name2)
    print(f"The following two text files are used: {f_name1} and {f_name2}")
    words_1 = dist_functions_v1.get_words_from_list(f_data1)
    words_2 = dist_functions_v1.get_words_from_list(f_data2)
    # print(words_2)
    # Word frequency calculation:
    freq_1 = dist_functions_v1.word_frequency_count(words_1)
    freq_2 = dist_functions_v1.word_frequency_count(words_2)

    # Calculating the angle between two text files
    angle = dist_functions_v1.calc_angle(freq_1, freq_2)
    print(angle)


if __name__ == "__main__":
    import cProfile
    #main()
    cProfile.run("main()")
