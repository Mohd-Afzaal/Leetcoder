class Solution:
    def isUgly(self, n: int) -> bool:
        key = [2,3,5]
        if n<1:
            return False
        for i in key:
            while n%i ==0:
                n//=i
        return n==1