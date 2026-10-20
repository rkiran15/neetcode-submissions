class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for let in s:
            s_dict[let] = s_dict.get(let,0) + 1
        t_dict = {}
        for let in t:
            t_dict[let] = t_dict.get(let,0) + 1
        if len(s_dict) != len(t_dict):
            return False
        for k in s_dict:
            if s_dict.get(k)!=t_dict.get(k):
                return False
        return True