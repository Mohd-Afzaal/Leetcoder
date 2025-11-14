def medianForEven(nums):
    mid1=int((len(nums)/2)-0.5)
    mid2=int((len(nums)/2)+0.5)
    return (nums[int(mid1)]+nums[int(mid2)])/2

def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1)%2==0:
        return medianForEven(nums1)
    else:
        mid=int(len(nums1)/2)
        return nums1[mid]

nums1=[1,2]
nums2=[3,4]

if __name__ == "__main__":
    print(findMedianSortedArrays(nums1,nums2))



