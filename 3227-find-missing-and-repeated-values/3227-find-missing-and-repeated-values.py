class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        found = set()
    
        dupe = 0

        for i in range(length):
            for j in range(length):
                if grid[i][j] in found:
                    dupe = grid[i][j]
                else:
                    found.add(grid[i][j])

        full = set(range(1, (length ** 2) + 1))
        return [dupe, list(full - found)[0]]
