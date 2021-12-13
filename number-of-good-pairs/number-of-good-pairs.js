/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let count = 0;
    for(let i = 0; i < nums.length; i++) {
        const temp = nums[i];
        for (let j = i+1; j < nums.length; j++) {
            if (temp === nums[j] && i < j) {
                count++;
            }
        }
    }
    return count;
};