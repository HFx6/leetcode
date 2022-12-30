#include <stdlib.h>
int* twoSum(int * nums, int numsSize, int target, int * returnSize) {
	
    for (int i = 0; i < numsSize; i++) {
		for (int x = i+1; x < numsSize; x++) {
			if(nums[i]+nums[x]==target){
                *returnSize=2;
                int * sums = malloc(2 * sizeof(int));
				sums[0]=i;
				sums[1]=x;
				return sums;
			}
		}
	}
	return 0;
}