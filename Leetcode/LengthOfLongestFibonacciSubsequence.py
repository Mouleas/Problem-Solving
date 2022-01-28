# Question Link
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in range(len(arr)):
            d[arr[i]] += 1
        
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                curr = arr[j]
                prev = arr[i]
                c = 2
                while curr+prev in d:
                    tmp = curr
                    curr += prev
                    prev = tmp
                    c += 1
                if c != 2:    
                    ans = max(c,ans)
        return ans
