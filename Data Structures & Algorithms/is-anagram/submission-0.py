class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # sort them
        s_list = []
        t_list = []
        for char in s:
            s_list.append(char)
        for char in t:
            t_list.append(char)
        t_list.sort()
        s_list.sort()
        return t_list == s_list
