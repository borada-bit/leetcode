
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        res = []
        res_index = 0

        for s in (strs):
            cnt = Counter(s)
            appended = False
            for lst in hmap[len(s)]:
                if cnt == lst[1]:
                    res[lst[0]].append(s)
                    appended = True
                    break
            if not appended:
                hmap[len(s)].append([res_index, cnt])
                res_index += 1
                res.append([s])

        return res 

