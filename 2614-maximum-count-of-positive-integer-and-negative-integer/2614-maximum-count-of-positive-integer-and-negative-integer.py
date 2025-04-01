class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ne=0
        pe=0
        for i in range(len(nums)):
            if nums[i]<0:
                ne+=1
            elif nums[i]>0:
                pe+=1
        return max(ne,pe)