class Solution:
    def isHappy(self, n: int) -> bool:
        current_value = str(n)
        max_itr = 0

        if n == 1:
            return True

        while int(current_value) != 1:
            result = 0

            for i in current_value:
                result += int(i) ** 2

            if result == 1:
                return True
            else:
                current_value = str(result)

            max_itr += 1

            if max_itr == 50:
                return False

        return False


solve = Solution()
print(solve.isHappy(2))
