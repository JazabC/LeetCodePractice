class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for i in range(0,len(nums)):
            if target - nums[i] in numsMap:
                return(i, numsMap[target-nums[i]])
            else:
                numsMap[nums[i]] = i
            
        return 0