from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(openCount, closeCount, current):
            if len(current) == 2 * n:
                result.append(current)
                return

            if openCount < n:
                backtrack(openCount + 1, closeCount, current + "(")

            if closeCount < openCount:
                backtrack(openCount, closeCount + 1, current + ")")

        backtrack(0, 0, "")
        return result


n = 3
sol = Solution()
print(sol.generateParenthesis(n))

# TC : O(4^n / sqrt(n))  (Catalan Number)
# SC : O(n)