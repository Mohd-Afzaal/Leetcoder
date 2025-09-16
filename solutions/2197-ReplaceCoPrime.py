import math
nums = [287,41,49,287,899,23,23,20677,5,825]
length = len(nums)

for i in range(length-1):
    print(i,i+1)
    hcf = math.gcd(nums[i],nums[i+1])
    if hcf != 1: 
        lcm_res = math.lcm(nums[i],nums[i+1])
        
        print(lcm_res)

        
        # index_to_delete = nums.index(i)
        # if index_to_replace in nums:
        #     continue
        # else:
        nums[i+1] = lcm_res
        nums[i] = 0

lst = [j for j in nums if j != 0] 
        
print(lst)