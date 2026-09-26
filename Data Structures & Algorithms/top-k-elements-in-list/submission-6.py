class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        bucket = [[] for i in range(len(nums)+1)]

        for key, value in num_map.items():
            bucket[value].append(key)

        result = []
        for element in reversed(bucket):
            if len(element) != 0 and len(result) < k:
                result += element

        return result

        