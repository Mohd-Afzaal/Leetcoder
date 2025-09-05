test1 = list(input("Enter number : "))
test2 = list(input("Enter number : "))

lst = []

for i,j in zip(test1,test2):
    lst.append(int(i))
    lst.append(int(j))

lst.sort()

print(lst)

_(2,3)