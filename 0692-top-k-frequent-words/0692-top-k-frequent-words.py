class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # one liner
        return [k for k,v in sorted(Counter(words).items(), key = lambda x:(-x[1], x))][:k]

        # Record frequency of strings
        mp = Counter(words)
        # Sorts the strings by their frequency in ascending order, then lexicographically
        mp = sorted(mp.items(), key=lambda x:(-x[1], x), reverse=False)
        # Returns the spliced list
        return [k for k,v in mp][:k]