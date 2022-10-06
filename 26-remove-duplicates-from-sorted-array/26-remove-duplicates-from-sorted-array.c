

int removeDuplicates(int* nums, int numsSize){ 
    int k = numsSize;
    int cur_num;
    int uniq_index = 0;
    
    for(int i = 0; i < numsSize; ++i) {
        cur_num = nums[i];
        while (i+1 < numsSize && cur_num == nums[i+1]) {
            // set to invalid
           nums[i+1] = 0xFF; 
           ++i; 
           --k;
        }
        nums[uniq_index] = cur_num;
        ++uniq_index;
    }
    
    return k;
}