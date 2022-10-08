class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = collections.defaultdict(int)
        
        for n in nums:
            h_map[n] += 1
            
        sorted_hmap = {key: val for key, val in sorted(h_map.items(), key=lambda item: item[1], reverse=True)}
        most_frequent = [0] * k
        
        i = 0 
        for key in sorted_hmap:
            if i < k:
                most_frequent[i] = key
            else:
                break
            i += 1
       
        return most_frequent