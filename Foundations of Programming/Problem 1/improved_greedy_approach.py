#!/usr/bin/env python3
""" Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

    Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

    Note: D can appear in any format (list, hash table, prefix tree, etc.)

    For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple".

      - The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
      - The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
      - The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""

def create_dictionary(string):
    dictionary = {}
    index = 0

    for ch in string:
        if ch in dictionary:
            dictionary[ch].append(index)
        else:
            dictionary[ch] = [index]
        index += 1
    return(dictionary)

def is_subsequence(word, dictionary):
    index_of_last_ch_found = -1
    for ch in word:
        if ch in dictionary and (dictionary[ch][-1] > index_of_last_ch_found):
            index = 0
            while index < len(dictionary[ch]):
                if index_of_last_ch_found is None or index_of_last_ch_found < dictionary[ch][index]:
                    index_of_last_ch_found = dictionary[ch][index]
                    break
                else:
                    index += 1

        else:
            return False
    return True

def replace_word_if_necessary(word, longest_word):
    if (longest_word is None) or (len(word) > len(longest_word)):
        longest_word = word
    return longest_word

def get_longest_word(s, d):
    dictionary = create_dictionary(s)
    longest_word = None

    for word in d:
        subsequence = is_subsequence(word, dictionary)
        if subsequence:
            longest_word = replace_word_if_necessary(word, longest_word)
    return longest_word
    
print(get_longest_word("abppplee", {"ale", "bale", "able", "apple", "kangaroo"}))
