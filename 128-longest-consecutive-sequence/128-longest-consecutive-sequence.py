class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = collections.defaultdict(list)
        
        for n in nums:
            answer[n] = [n]
        
        dict_len = len(answer)
        curr_num = 0;
        for n in nums:
            curr_num = n - 1
            #print(f"this is it {curr_num=}")
            while curr_num in answer:
                answer[n] += answer.pop(curr_num)
                #print(f"whiling {curr_num=} {n=}") 
                curr_num -= 1
                dict_len -= 1
        print(answer)
        max_answer = 0
        for val in answer.values():
            print(val)
            print(type(val))
            if len(val) > max_answer:
                max_answer = len(val)
    
            
                    
        return max_answer
        