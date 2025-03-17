class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        i=(len(nums1)+len(nums2))//2
        if len(l)%2==1:
            return l[i]
        else:
            return (l[i-1]+l[i])/2