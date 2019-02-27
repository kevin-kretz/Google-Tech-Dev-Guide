class Main:
    def create_dictionary(string):
        dictionary = {}
        index = 0

        for letter in string:
            if letter in dictionary:
                dictionary[letter].append(index)
            else:
                dictionary[letter] = [index]
            index += 1
        return(dictionary)
    
    def get_word_is_substring(word, dictionary):
        index_of_last_letter_found = None
        for letter in word:
            if letter in dictionary and (index_of_last_letter_found is None or dictionary[letter][-1] > index_of_last_letter_found):
                index = 0
                while index < len(dictionary[letter]):
                    if index_of_last_letter_found is None or index_of_last_letter_found < dictionary[letter][index]:
                        index_of_last_letter_found = dictionary[letter][index]
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
        dictionary = Main.create_dictionary(s)
        longest_word = None
        
        for word in d:
            word_is_substring = Main.get_word_is_substring(word, dictionary)
            if word_is_substring:
                longest_word = Main.replace_word_if_necessary(word, longest_word)
        print(longest_word)

Main.get_longest_word("abppplee", {"ale", "bale", "able", "apple", "kangaroo"})
