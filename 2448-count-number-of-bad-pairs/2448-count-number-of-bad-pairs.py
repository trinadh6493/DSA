class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total_pairs=0
        good_pairs=0
        offsets_counter=defaultdict(int)

        for i in range(len(nums)):
            total_pairs+=i
            offset=nums[i]-i
            good_pairs+=offsets_counter[offset]
            offsets_counter[offset]+=1

        return total_pairs-good_pairs