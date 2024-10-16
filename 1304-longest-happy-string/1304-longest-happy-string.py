# s only contains a, b, c
# cannot contain aaa, bbb, ccc (three of the same letter)
# contains at most the number given in the parameters (a # of a's, etc.)
# return the longest possible string

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret, heap = "", []

        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(heap, (count, char))

        while heap:
            count, char = heapq.heappop(heap)
            if len(ret) > 1 and ret[-1] == ret[-2] == char:
                if not heap:
                    break
                
                cCount, cChar = heapq.heappop(heap)
                ret += cChar
                cCount += 1
                if cCount:
                    heapq.heappush(heap, (cCount, cChar))
            else:
                ret += char
                count += 1
            if count:
                heapq.heappush(heap, (count, char))
        return ret