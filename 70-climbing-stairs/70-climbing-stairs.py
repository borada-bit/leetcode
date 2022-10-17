class Solution:
    hmap = collections.defaultdict(int)
    hmap [0] = 0;
    hmap[1] = 1
    hmap[2] = 2
    
    def climbStairs(self, n: int) -> int:
        
        if n:
            self.climbStairs(n-1)
        
        if n not in self.hmap:
            self.hmap[n] = self.hmap[n-1] + self.hmap[n-2]
        
        return self.hmap[n]
        
        pass
    
