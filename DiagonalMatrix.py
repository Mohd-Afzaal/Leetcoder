lst = ["flower","flow","flight"]

pref = lst[0]
pref_length = len(pref)

for i in lst[1:]:
    while pref != i[0:pref_length]:
        pref_length -= 1
        
        if pref_length == 0:
            print("")
        
        pref = pref[0:pref_length]

print(pref)

