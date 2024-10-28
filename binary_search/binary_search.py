class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + ((right - left) // 2)

            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1


if __name__ == "__main__":
    solution = Solution()

    solution.search([-1, 0, 2, 4, 6, 8], 4)
    solution.search([-1, 0, 2, 4, 6, 8], 3)
