# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list):
        anagrams = []
        for word in list:
            if sorted(word) == sorted(self.word):
                anagrams.append(word)
        return anagrams

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
