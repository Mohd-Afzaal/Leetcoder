class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lst1 = text.split(" ")
        lst2 = []
        for i in range(1,len(lst1)-1):
            if lst1[i] == second and lst1[i-1] == first:
                lst2.append(lst1[i+1])
        return lst2