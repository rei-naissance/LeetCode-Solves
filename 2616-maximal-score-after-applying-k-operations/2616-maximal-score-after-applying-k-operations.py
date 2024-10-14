class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        
        for x in nums:
            heapq.heappush(hp, -x)

        total = 0
        for _ in range(k):
            holder = -heapq.heappop(hp)
            total += holder
            holder = (holder + 2) // 3
            heapq.heappush(hp, -holder)

        return total