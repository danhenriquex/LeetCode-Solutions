from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return [[""]]

        anagrams: dict[str, list] = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)

        result = []

        for values in anagrams.values():
            result.append(values)

        return result

    def groupAnagrams_hastable(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()


if __name__ == "__main__":
    solve = Solution()
    # solve.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    solve.groupAnagrams_hastable(["act", "pots", "tops", "cat", "stop", "hat"])
    # solve.groupAnagrams([""])
    # solve.groupAnagrams(["a"])
