class Solution:

    def encode(self, strs: List[str]) -> str:
        big_word = ""

        for word in strs:
            big_word += str(len(word)) + "#" + word

        print(f'{big_word =}')
        return big_word

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_starts = j + 1
            word_ends = word_starts + length

            decoded_strs.append(s[word_starts: word_ends])

            i = word_ends

        return decoded_strs

