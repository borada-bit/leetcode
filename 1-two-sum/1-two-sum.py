class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} 
        for i, num in enumerate(nums):
            if num in hash_map:
                # assumes only two equal integers in list exist
                another_index = hash_map[num]
                hash_map[num] = [another_index, i]
            else:
                hash_map[num] = i
    
        for number, index in hash_map.items():
            searched_number = target - number
            if searched_number in hash_map:
                if searched_number != number:
                    return [index, hash_map[searched_number]]
                elif searched_number == number and type(hash_map[searched_number]) == list:
                    return [hash_map[searched_number][0], hash_map[searched_number][1]] 
        