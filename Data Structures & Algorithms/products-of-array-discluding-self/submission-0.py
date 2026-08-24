class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # 1. calculating prefix for all in nums

        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # 2. output from n-1 till before n - reverse, updating inplace in output array

        suffix = 1
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]


        return output
