user_list = list(input("Enleetcodeter number:"))
remove = int(input("Enter number:"))
lst = []
k = 0

for i in user_list:
    lst.append(int(i))

for j in lst:
    if remove != j:
        k+=1

print(k)

