class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for char1, char2 in zip_longest(word1, word2, fillvalue = ''):
            result.append(char1)
            result.append(char2)
        return "".join(result)