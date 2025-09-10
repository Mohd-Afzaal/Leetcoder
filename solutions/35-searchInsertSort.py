# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
lst = list((input("Enter numbers: ")))
key = int(input("Enter Number: "))
lst1 = []

for i in lst:
    lst1.append(int(i))

if key in lst1:
    for i in range(len(lst1)):
        if lst1[i]==key:
            print(i)

elif key not in lst1:
    index = len(lst1)
    for i in range(len(lst1)):
        if key <= lst1[i]:
            index = i
            break
    print(index)
