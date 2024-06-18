class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        if len(word1) >= len(word2):
            l = word1
            s = word2
        else:
            l = word2
            s = word1

        merge = ""
        while i < len(s):
            merge = merge + word1[i] + word2[i]
            i = i + 1
            if i >= len(s):
                merge = merge + l[i:]
                i = i + 1
        return merge
