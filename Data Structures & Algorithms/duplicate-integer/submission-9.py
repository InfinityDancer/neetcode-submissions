class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # print(f'{nums =}')
        nums.sort()
        # print(f'{nums =}')

        if len(nums) == 0:
            return False

        prev = nums[0]
        # cur = nums[1:]

        for cur in nums[1 :]:
            # print(f'{prev =}, {cur =}')
            
            if prev == cur:
                # has duplicates
                return True


            prev = cur

        return False























        # check_dups = set(nums)

        # if len(check_dups) == len(nums):
        #     return False
        # else:
        #     return True
        

