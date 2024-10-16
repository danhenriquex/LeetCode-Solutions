class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1]


if __name__ == "__main__":
    solution = Solution()

    solution.twoSum([2, 7, 11, 15], 9)
    solution.twoSum([1, 2, 3, 4], 3)
    solution.twoSum([2, 3, 4], 6)
    solution.twoSum([100, 200, 300, 500], 500)
