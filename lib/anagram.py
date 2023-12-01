# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word.lower()
    
    def match(self, source_list):
        new_list = list()
        x = sorted(self.word)
        for letter in x:
            new_list.append(letter)
        matched_anagrams = []
        for name in source_list:
            if sorted(name.lower()) == x and name.lower() != self.word:
                matched_anagrams.append(name)
        return matched_anagrams
                
                
                