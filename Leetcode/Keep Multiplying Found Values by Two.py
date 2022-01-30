# Question Link
# https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int],t: int) -> int:
        while t in nums:
            t = t*2
        return t
