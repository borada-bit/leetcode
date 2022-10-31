class Solution:
    def reverseBits(self, n: int) -> int:
        powers = [2**i for i in range(32)]
        powers_len = len(powers)
        ans = 0
        
        for i, p in enumerate(powers):
            if n & p == p:
                ans |= (powers[powers_len-i-1])
                
        return ans
        