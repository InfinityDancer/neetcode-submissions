class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialise empty dict
        anagram_dict = {}

        # access current word in strs
        for string in range(len(strs)):
            
            # alphabetically sort current string
            sorted_string = "".join(sorted(strs[string]))

            # if sorted string in dict
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(strs[string])

            # else if sorted string not a key in dict
            else:
                anagram_dict[sorted_string] = [strs[string]]
        
        # construct output array
        output_array = []

        for key in anagram_dict:
            output_array.append(anagram_dict[key])

        return output_array