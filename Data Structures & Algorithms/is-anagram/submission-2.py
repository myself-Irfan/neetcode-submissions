class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        set_of_letters = set(s)

        s_map = {}
        t_map = {}

        for char in set_of_letters:
            s_map[char] = s.count(char)
            t_map[char] = t.count(char)

        return s_map == t_map