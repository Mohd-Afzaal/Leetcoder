class Solution:
    def hammingWeight(self, n: int) -> int:
        remainder = 0
        count = 0
        while n:
            remainder = n%2
            if remainder == 1:
                count+=1
            n //=2
        return count 

# Alternative solution using bit manipulation
    def hammingWeightBitManipulation(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count   
    
    def hammingWeightBitManipulation2(self, n: int) -> int:
        count = 0
        while n:
            n = n&(n-1)
            count+=1
        return count       