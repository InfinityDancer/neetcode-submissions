class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = {}

        # construct dict
        for current_num in nums:
            nums_dict[current_num] = nums_dict.get(current_num, 0) + 1

        # print(f'{nums_dict =}')

        # sort keys by dict values (in descending order)
        sorted_keys = sorted(nums_dict.keys(), key = lambda x: nums_dict[x], reverse = True)

        # print(f'{nums_dict =}')

        # return top k elements
        return sorted_keys[:k]