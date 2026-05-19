class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dups = True

        if len(nums) == len(set(nums)):
            has_dups = False

        return has_dups