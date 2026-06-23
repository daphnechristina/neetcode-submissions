class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import numpy
        s_arr = list(s)
        t_arr = list(t)
        s_sorted = sorted(s_arr)
        t_sorted = sorted(t_arr)
        return s_sorted == t_sorted