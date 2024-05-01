class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        n = word.index(ch)
        word = word[:n+1][::-1] + word[n+1:]
        return word
