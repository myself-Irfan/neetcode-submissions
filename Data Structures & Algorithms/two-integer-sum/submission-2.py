class Solution:
    def twoSum(self, num_list: List[int], target: int) -> List[int]:
        num_map = {}
  
        for idx, num in enumerate(num_list):
            if target-num in num_map: 
                return [num_map[target-num], idx]
            num_map[num] = idx