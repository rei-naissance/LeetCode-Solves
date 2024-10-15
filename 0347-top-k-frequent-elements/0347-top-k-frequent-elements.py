class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequencies
        mp = Counter(nums)
        # sort map according to the frequencies using lambda
        mp = sorted(mp.items(), key = lambda x:x[1], reverse=True)
        # return spliced list of keys
        return [k for (k,v) in mp][:k]

        # one liner
        # return [k for k,v in sorted(Counter(nums).items(), key = lambda x:x[1], reverse=True)][:k]
