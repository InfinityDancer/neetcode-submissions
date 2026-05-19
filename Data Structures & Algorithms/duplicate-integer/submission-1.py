class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dups = True

        if len(nums) == len(set(nums)):
            print(f'{nums =}')
            print(f'{set(nums) =}')
            has_dups = False

        return has_dups

        # if

        # for i in range(len(nums)):
        #     if i in set(nums):
        #         print(i)