nums = [1,2,2,3,1,4]
temp = list(set(nums))

freq = {} 


count = 0
for i in range(len(temp)+1):
    freq.update({nums[i]:0})

for i in range(3):
    freq[i] = count + 1
    count+=1

print(freq)