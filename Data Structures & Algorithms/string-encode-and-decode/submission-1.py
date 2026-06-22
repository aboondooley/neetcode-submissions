class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        special = '#'
        encoded = str(n)+special
        words_str = ''
        for word in strs:
            encoded = encoded + str(len(word)) + special
            words_str+=word
        
        return encoded+words_str


    def decode(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return ['']
        
        n, index = 0, 0
        while index < len(s) and s[index] != '#':
            index+=1
        n = int(s[:index])
        index+=1

        lengths = []
        for i in range(n):
            last = index
            while index < len(s) and s[index] != '#':
                index+=1
            lengths.append(int(s[last:index]))
            index+=1

        words = []
        for l in lengths:
            last = index
            index+=l
            word = s[last:index]
            words.append(word)

        return words
            



