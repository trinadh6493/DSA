class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            v=target-nums[i]
            if v in d:
                return [i,d[v]]
            else:
                d[nums[i]]=i