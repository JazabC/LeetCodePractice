class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        i = 0
        j = len(nums)-1
        
        while i <= j:
            mid = int((i+j)//2)
            
            if nums[mid] == target:
                start = mid
                end = mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == target:
                    end += 1
                    
                return [start, end]
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return [-1,-1]
        