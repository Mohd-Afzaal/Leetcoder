# convert roman numerals to int

roman = input("Enter roman numeral:")
value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

result = 0

for i,j in zip(roman,roman[1:]):
    if value[i] < value[j]:
        result -= value[i] 
    else:
        result += value[i]
    
out = result + value[roman[-1]]

print(out)