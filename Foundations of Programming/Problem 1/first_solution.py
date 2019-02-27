class Main:
  def get_longest_word(s, d):
      longest_word_found = None
        
      for word in d:
        index_of_first_letter = s.find(word[0])

        if (index_of_first_letter != -1):
            last_index_found = index_of_first_letter
            i = 1;
            while (i < len(word)):
                next_letter_index = s[last_index_found:].find(word[i])
                if next_letter_index != -1:
                    last_index_found = next_letter_index
                    i += 1
                else:
                    break
            if i == len(word):
                if longest_word_found is None or len(word) > len(longest_word_found):
                    longest_word_found = word      

      return(longest_word_found)

print(Main.get_longest_word("abppplee", {"able", "ale", "apple", "bale", "kangaroo"}))
