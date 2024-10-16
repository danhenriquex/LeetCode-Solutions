import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []

        s = re.sub(r"[^a-zA-Z0-9]", "", s)

        for char in s:
            if char.isalnum():
                stack.append(char.lower())

        reversed_string = ""
        while stack:
            reversed_string += stack.pop()

        value = s.replace(" ", "").lower()

        if reversed_string == s.replace(" ", "").lower():
            print("True")
            return True
        else:
            print("False")
            return False

    def isPalindromeOptimal(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        return newStr == newStr[::-1]

    def isPalindromePointers(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not self.alphaNum(s[left]):
                left += 1

            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                print("False")
                return False
            left, right = left + 1, right - 1

        print("True")
        return True

    def alphaNum(self, char):
        return (
            ord("A") <= ord(char) <= ord("Z")
            or ord("a") <= ord(char) <= ord("z")
            or ord("0") <= ord(char) <= ord("9")
        )


if __name__ == "__main__":
    solution = Solution()
    solution.isPalindromePointers("cat tac")
    solution.isPalindromePointers("Was it a car or a cat I saw?")
