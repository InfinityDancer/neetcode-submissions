class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letter_map = {}

        for letter in s:
            letter_map[letter] = letter_map.get(letter, 0) + 1

        for letter in t:
            if letter not in letter_map:
                return False
            
            letter_map[letter] -= 1

            if letter_map[letter] < 0:
                return False

        return True