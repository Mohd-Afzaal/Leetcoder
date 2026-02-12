/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    *returnSize=2;
    int *arr=calloc(2,sizeof(int));
    long int ab = 0, right_most;

        for(int i=0;i < numsSize; i++ ){
            ab^=nums[i];
        }
        right_most = ab & -ab;

        for(int j = 0; j<numsSize; j++){
            if (nums[j]&right_most){
                arr[0]^=nums[j];
            }
            else{
                arr[1]^=nums[j];
            }
        }
    return arr;  
}