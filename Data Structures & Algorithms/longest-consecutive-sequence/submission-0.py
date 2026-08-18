class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0

        nums_set = set(nums)
        checked_set = set()

        for cur_num in nums_set:
            # print(f'{cur_num =}')
            cur_seq = 1
            next_in_seq = 1

            if cur_num not in checked_set:

                print(f'{cur_num + next_in_seq =}')

                while cur_num + next_in_seq in nums_set:
                    # print(f'{cur_num + next_in_seq =}')

                    checked_set.add(cur_num + next_in_seq)

                    cur_seq += 1
                    next_in_seq += 1

                if cur_seq > longest_seq:
                    longest_seq = cur_seq

                print(f'{cur_seq =}')
                
                continue

        return longest_seq