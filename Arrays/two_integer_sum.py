import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from decorators.timer import measure_time


class Solution:

    @measure_time
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        size = len(nums)

        for i in range(size):
            dictionary[nums[i]] = i

        for i in range(size):
            diff = target - nums[i]

            if diff in dictionary and dictionary[diff] != i:
                print(f"result: {i}, {dictionary[diff]}")
                return [i, dictionary[diff]]


if __name__ == "__main__":
    sol = Solution()
    sol.twoSum([2, 7, 11, 15], 9)
    sol.twoSum([2, 5, 5, 11], 10)
