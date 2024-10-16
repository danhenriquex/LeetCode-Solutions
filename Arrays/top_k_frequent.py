class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        table: dict = {}

        for num in nums:
            table[num] = 0

        for num in nums:
            table[num] = table[num] + 1

        tupleList: list = []

        for key, value in table.items():
            tupleValue = (value, key)

            tupleList.append(tupleValue)

        tupleSorted = sorted(tupleList, reverse=True)

        results: list = []

        for value in range(k):
            results.append(tupleSorted[value][1])

        return results

    def topKFrequentOptimal(self, nums: list[int], k: int) -> list[int]:
        count: dict = {}
        freq: list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for value, count in count.items():
            freq[count].append(value)

        results: list = []

        for count in range(len(freq) - 1, 0, -1):
            for value in freq[count]:
                results.append(value)

                if len(results) == k:
                    return results


if __name__ == "__main__":
    solution = Solution()
    solution.topKFrequentOptimal([1, 1, 5, 5, 5, 3, 3], 2)
    solution.topKFrequentOptimal([1, 2], 2)
    solution.topKFrequentOptimal([1, 1, 1, 2, 2, 3], 2)
    solution.topKFrequentOptimal([7, 7], 1)
