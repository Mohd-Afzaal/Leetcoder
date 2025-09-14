a = "1"
b = "111"
carry = 0
res = ""

a,b = a[::-1], b[::-1]

for i in range(max(len(a),len(b))):
    digitA = ord(a[i]) - ord("0") if i < len(a) else 0
    digitB = ord(b[i]) - ord("0") if i < len(b) else 0
    print(digitA,digitB) 
    sum = digitA + digitB + carry
    char = str(sum%2)
    res = char + res
    carry = sum//2

if carry:
    res = "1" + res

print(res)
