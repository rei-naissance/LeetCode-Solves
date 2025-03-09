class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        invalid_count = 0

        for i in range(k - 1):
            if colors[i] == colors[i + 1]:
                invalid_count += 1

        for i in range(n):
            if invalid_count == 0:
                count += 1
            
            left = i
            right = (i + k - 1) % n  

            if colors[right] == colors[(right + 1) % n]:
                invalid_count += 1  

            if colors[left] == colors[(left + 1) % n]:
                invalid_count -= 1  

        return count
