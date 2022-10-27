

// [0 .. n]
int missingNumber(int* nums, int numsSize){
    int temp = 0;
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        ans ^= temp ^ nums[i];
        temp++;
    }
    return ans^temp;
}