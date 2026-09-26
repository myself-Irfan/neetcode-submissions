from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        num_map_2 = [(-value, key) for key, value in num_map.items()]
        heapify(num_map_2)

        num_map_3 = []
        for x in range(0, k):
            element = heappop(num_map_2)
            num_map_3.append(element[1])


        return num_map_3