class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and right > left:
                        left += 1

        # print("Result: ", result)
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.threeSum([-1, 0, 1, 2, -1, -4])
