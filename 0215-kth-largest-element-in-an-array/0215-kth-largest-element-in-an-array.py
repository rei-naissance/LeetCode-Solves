class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        for _ in range(k):
            x = -heapq.heappop(max_heap)

        return x