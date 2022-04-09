class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1
        print(letters)
        for r in ransomNote:
            res = letters.get(r, 0)
            if res == 0:
                return False
            else:
                letters[r] = letters.get(r, 0) - 1
        return True
                
