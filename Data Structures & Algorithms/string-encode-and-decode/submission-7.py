class Solution:

    def encode(self, strs: List[str]) -> str:
        big_word = ""

        for word in strs:
            big_word += str(len(word)) + "#" +word
        return big_word

    def decode(self, s: str) -> List[str]:
        decode_strs = []

        i = 0
        while i < len(s):
            hash_search = i

            while s[hash_search] != "#":
                hash_search += 1

            word_start = hash_search + 1
            word_length = int(s[i: hash_search])
            word_end = word_start + word_length

            decode_strs.append(s[word_start: word_end])

            i = word_end

        return decode_strs