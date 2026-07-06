class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        if len(nums) == 0:
            return False

        prev = nums[0]

        for cur in nums[1 :]:
            
            if prev == cur:
                # has duplicates
                return True

            prev = cur

        return False