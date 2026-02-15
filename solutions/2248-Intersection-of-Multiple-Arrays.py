class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = set(nums[0])
        for i in nums:
            seen &= set(i)
        res = list(seen)
        res.sort()
        return res
    
    def intersection2(self, nums: List[List[int]]) -> List[int]:
        seen = {}
        lst = []
        for i in nums:
            for j in i:
                if j not in seen:
                    seen[j] = 1
                else:
                    seen[j] += 1
        
        for k in seen:
            if seen[k] == len(nums):
                lst.append(k)
        lst.sort()
        return lst 