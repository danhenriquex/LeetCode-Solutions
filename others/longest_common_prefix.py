class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):  # executa 2 vezes
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]

        return res


solve = Solution()

# result = solve.longestCommonPrefix(["dog", "doter", "dogshoe"])
# result = solve.longestCommonPrefix(["dog", "racecar", "car"])
# result = solve.longestCommonPrefix(["flower", "flower", "flower", "flower"])
# result = solve.longestCommonPrefix(["fwer", "fl", "fht"])
# result = solve.longestCommonPrefix(["flower", "flow", "flight"])
result = solve.longestCommonPrefix(["ab", "a"])

print(result)
