""" Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
    Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
    Note: D can appear in any format (list, hash table, prefix tree, etc.)
    For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple".
      - The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
      - The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
      - The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""

from collections import defaultdict

def create_S_dictionary(S):
    """Returns a dictionary of a string (S), using each character in S (ch) as keys, and a list of all of the character's indexes (i) as the values."""
    d = defaultdict(list)
    for i, ch in enumerate(S):
        d[ch].append(i)    
    return d

def is_subsequence(w, S):
    """Returns a boolean value of whether a word (w) is a subsequence of a string (S)"""
    last_found_i = -1

    for ch in w:
        if ch in S and S[ch][-1] > last_found_i:
            for i in S[ch]:
                if last_found_i < i:
                    last_found_i = i
                    break
        else:
            return False
    return True

def get_longest_subsequence(S, D):
    """Returns the longest word, in a set of words (D), that is a subsequence of a string (S)"""
    S = create_S_dictionary(S)
    D = sorted(D, key=len, reverse=True)
    for w in D:
        if is_subsequence(w, S):
            return w
            
print(get_longest_subsequence("babppplee", {"ale", "able", "bale", "apple", "kangaroo"}))
