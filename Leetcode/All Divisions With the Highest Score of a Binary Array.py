# Question Link
# https://leetcode.com/contest/weekly-contest-278/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        x,y = 0,0
        for i in nums:
            if i == 1:
                y += 1
            
        ans = defaultdict(list)
        ans[y].append(0)
        maxx = y
        for i in range(len(nums)):
            if nums[i] == 1:
                y -= 1
            else:
                x += 1
            
            maxx = max(x+y,maxx)
            ans[x+y].append(i+1)
        
        return ans[maxx]
        
