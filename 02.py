x = -121

lst = [d for d in str(x)]

print(lst[::-1])
print(lst)

if(lst == lst[::-1]):
    print(True)
else:
    print(False)

