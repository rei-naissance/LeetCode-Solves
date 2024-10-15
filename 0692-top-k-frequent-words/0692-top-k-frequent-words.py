class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        mp = sorted(mp.items(), key=lambda x:(-x[1], x), reverse=False)
        return [k for k,v in mp][:k]