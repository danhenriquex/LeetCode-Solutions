import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1

        return res

    def minEatingSpeedBruteForce(self, piles: List[int], h: int) -> int:
        speed = 1

        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                print("Speed: ", speed)
                return speed

            speed += 1


if __name__ == "__main__":
    solution = Solution()

    solution.minEatingSpeed([3, 6, 7, 11], 8)
    solution.minEatingSpeed([1, 4, 3, 2], 9)
    solution.minEatingSpeed([25, 10, 23, 4], 4)
