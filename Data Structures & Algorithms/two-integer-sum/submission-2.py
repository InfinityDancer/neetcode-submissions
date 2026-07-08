class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            # print(f'{num =}, {i =}')

            complement = target - num

            if complement in index_map:
                # print(f'{index_map =}')
                # print(f'{complement =}')
                return [index_map[complement], i]

            index_map[num] = i
