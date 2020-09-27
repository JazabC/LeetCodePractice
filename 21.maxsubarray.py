class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurr = nums[0]
        maxGlobal = nums[0]
        
        for i in nums[1:]:
            maxCurr = max(i, maxCurr+i)
            maxGlobal = max(maxGlobal, maxCurr)
            
        return maxGlobal