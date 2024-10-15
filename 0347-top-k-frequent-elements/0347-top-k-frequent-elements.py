class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        keys = sorted(mp.items(), key = lambda x:x[1], reverse=True)
        return [k for (k,v) in keys][:k]

        # return [k for k,v in sorted(.items(), key = lambda x:x[1])]
