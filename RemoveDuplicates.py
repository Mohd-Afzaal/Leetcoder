user = list(input("Enter number:"))
lst = []
k = 0

for i in user:
    lst.append(int(i))

lst.sort()
length = len(lst)

lst1 = list(set(lst))

while len(lst1)!= length:
    lst1.append("_")

print(lst1)
