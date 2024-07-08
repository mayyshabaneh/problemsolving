class Solution:
    def lengthOfLongestSubstring(self, s):
        maxcount = 0
        temp = []
        start = 0

        for i in range(len(s)):
            if s[i] in temp:
                start = temp.index(s[i]) + 1
                temp = temp[start:] 
            temp.append(s[i])
            if maxcount < len(temp):
                maxcount = len(temp)

        return maxcount