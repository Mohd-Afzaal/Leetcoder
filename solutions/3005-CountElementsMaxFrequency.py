
def max_count(num, lst):
    count = 0
    for i in range(len(nums)):
        if num == lst[i]:
            count+=1
    return count
    

nums = [2,4,4,5,3,2,9,2,2,4,4,3,3]
temp = list(set(nums))
max_freq_count = 0
freq = []

for i in temp:
    freq.append(max_count(i,nums))

max_freq = max(freq)

for j in freq:
    if max_freq == j:
        max_freq_count += max_freq 

print(max_freq_count)



