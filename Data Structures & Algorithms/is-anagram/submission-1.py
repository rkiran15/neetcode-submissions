class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict = {}
        for let in s:
            s_dict[let] = s_dict.get(let,0) + 1
        for let in t:
            if s_dict.get(let,0) == 0:
                return False
            else:
                s_dict[let] = s_dict[let] - 1
        for k in s_dict:
            if s_dict[k] != 0:
                return False
        return True
