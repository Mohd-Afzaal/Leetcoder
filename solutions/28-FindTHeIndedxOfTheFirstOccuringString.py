haystack = list(input("Enter string: "))

needle = list(input("Enter string: "))

for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i+len(needle)] == needle:
        print(i)
        break 
    else:
        print(-1)


