class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(f'{i =}')
            for j in range(len(nums)):
                if target - nums[i] == nums[j]:
                    if i!= j:
                        return [i, j]