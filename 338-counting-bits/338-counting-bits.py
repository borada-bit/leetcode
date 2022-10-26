class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        
        ans = [0, 1]
        bits_index = 0;
        for i in range(2, n+1):
            if (i & (i-1)) == 0:
                bits_index = 0
            ans.append(ans[bits_index] + 1)
            bits_index += 1
        
        return ans
