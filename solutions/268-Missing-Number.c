int missingNumber(int* nums, int numsSize) {
    int currSum = 0, resSum = 0;
    for(int i=0;i<numsSize;i++){
        currSum+=nums[i];
        resSum+=i+1;
    }
    return resSum - currSum;
}