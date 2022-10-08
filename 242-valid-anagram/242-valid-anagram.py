class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmap = {}
        for i in range(len(s)):
            if s[i] != t[i]:
                if s[i] in hmap: hmap[s[i]] += 1
                else: hmap[s[i]] = 1
                    
                if t[i] in hmap: hmap[t[i]] -= 1
                else: hmap[t[i]] = -1
                
        return all([val == 0 for val in hmap.values()])
        