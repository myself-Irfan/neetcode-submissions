class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        set_of_letters = set(s)

        s_dict = {}
        t_dict = {}

        for letter in set_of_letters:
            s_dict[letter] = s.count(letter)
            t_dict[letter] = t.count(letter)
        
        return s_dict == t_dict
        