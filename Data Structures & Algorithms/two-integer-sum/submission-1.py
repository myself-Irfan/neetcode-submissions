class Solution:
    def twoSum(self, num_list: List[int], target: int) -> List[int]:
        for idx, num in enumerate(num_list):
            for i in range(idx+1, len(num_list)):
                if num + num_list[i] == target:
                    return [idx, i]
