class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        lst = []
        powr = 0 
        while n:
            temp = n%10
            if temp == 0:
                powr+=1
            else:
                lst.append(temp*(10**powr))
                powr+=1
            n//=10
            
        return lst[::-1]

