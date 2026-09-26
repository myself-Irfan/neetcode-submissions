from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        num_map_2 = [(value, key) for key, value in num_map.items()]
        heapify(num_map_2)

        for _ in range(len(num_map_2)-k): 
            heappop(num_map_2)
        
        return [x[1] for x in num_map_2]