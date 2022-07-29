from typing import List
from itertools import permutations

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1

        path = m * 'B' + n * 'D'

        possible_paths = permutations(path)
        possible_paths = set(possible_paths)

        n_paths = 0

        for path in possible_paths:
            x = 0
            y = 0
            aux = True
            for c in path:
                if c == 'B':
                    x += 1
                    if obstacleGrid[x][y] == 1:
                        aux = False
                else:
                    y += 1
                    if obstacleGrid[x][y] == 1:
                        aux = False

            if aux:
                n_paths += 1


        return n_paths


# [1][0] -> baixo
# [0][1] -> direita
#




def main():
    sol = Solution()
    answ = sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(answ)


main()
