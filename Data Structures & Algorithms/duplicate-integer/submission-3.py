class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dups = set(nums)

        if len(check_dups) == len(nums):
            return False

        else:
            return True
        