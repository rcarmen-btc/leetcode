class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power_list = []
        for row in mat:
            power_list.append(sum(row))
        print(power_list)
        
        res = []
        i = 0
        while len(res) < k:
            for j, l in enumerate(power_list):
                if len(res) >= k:
                    return res
                if i == l:
                    res.append(j)
            i += 1
        return res