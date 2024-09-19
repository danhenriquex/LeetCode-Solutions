class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        print(strs)


if __name__ == "__main__":
    solve = Solution()
    solve.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    solve.groupAnagrams([""])
    solve.groupAnagrams(["a"])
