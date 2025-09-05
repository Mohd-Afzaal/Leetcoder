a = "1326#"
lst = list(a)
result = []
print(result)
print(lst)
i = 0
while i < len(lst):
    if  i+2< len(lst) and lst[i+2] == "#":
        num = int(lst[i:i+2])
        result.append(chr(num+96))
        i+=3

    else:
        num = int(lst[i])
        result.append(chr(num+96))
        i+=1

print(result) 