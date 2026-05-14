class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_encoded_list = {}
        for word in strs:
            char_count = {}
            for letter in word:
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1

            key = frozenset(char_count.items())

            if key in word_encoded_list:
                word_encoded_list[key].append(word)
            else:
                word_encoded_list[key] = [word]
        
        output = []
        for angram in word_encoded_list:
            output.append(word_encoded_list[angram])

        return output
