num = int(input("Enter n: "))

prev,curr = 1,1

for i in range(num-1):
    temp = curr
    curr = prev+curr
    prev = temp

print(curr)

