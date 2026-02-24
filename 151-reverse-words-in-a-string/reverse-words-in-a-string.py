class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        start = 0 
        end = len(x) - 1
        while start < end:
            x[end], x[start] = x[start], x[end]
            start += 1
            end -= 1
        return " ".join(x)