class Solution:
    # Hash Map
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen:
                return True
            seen[i] = 1
        return False
    
    # One Liner
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))