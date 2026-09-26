class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for idx, string in enumerate(strs):
            sorted_word = ''.join(sorted(string))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = [] + [string]
            else:
                anagram_map[sorted_word].append(string)
        
        return [v for k, v in anagram_map.items()]