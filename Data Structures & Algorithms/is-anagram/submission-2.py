class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dict, s_dict = {}, {}
        if len(s) != len(t): return False

        for i in range(len(s)):
            sc = s[i]
            if sc in s_dict: s_dict[sc]+=1
            else: s_dict[sc] = 1
            tc = t[i]
            if tc in t_dict: t_dict[tc]+=1
            else: t_dict[tc] = 1

        return s_dict == t_dict
                