class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Construct and populate the dictionary
        nums_dict = {}
        for num in nums:
            # .get(num, 0) returns 0 if the number isn't in the dict yet
            nums_dict[num] = nums_dict.get(num, 0) + 1
            
        # 2. Sort the keys by their dictionary values, in reverse (descending) order
        sorted_keys = sorted(nums_dict.keys(), key=lambda x: nums_dict[x], reverse=True)
        
        # 3. Return the top k elements
        return sorted_keys[:k]