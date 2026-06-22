class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = []
        alike = []

        for word in strs:
            curr_freq = {}
            for c in word:
                if c in curr_freq:
                    curr_freq[c]+=1
                else:
                    curr_freq[c] = 1
            found = False
            i = 0
            while not found and i < len(freq):
                if curr_freq == freq[i]:
                    alike[i].append(word)
                    found = True
                i+=1
            if not found:
                freq.append(curr_freq)
                alike.append([word])
            
        return alike
                
                
