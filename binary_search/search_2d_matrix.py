class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        left, right = 0, rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // columns][mid % columns]

            if mid_element == target:
                print("Valor encontrado: ", mid_element)
                return True

            if mid_element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()
    solution.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)
    solution.searchMatrix([[1]], 1)
