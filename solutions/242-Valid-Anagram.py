class Solution:
    # Sorted
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s)==sorted(t)

    # counter
    def isAnagramCounter(self, s: str, t: str) -> bool:
        # makes a hash map of the characters and their counts, then compares the two hash maps
        return Counter(s)==Counter(t)

    # replace
    # replaces each character in s with an empty string, then checks if t is empty
    def isAnagramReplace(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            t = t.replace(i,'',1)
        return t == '' 

        