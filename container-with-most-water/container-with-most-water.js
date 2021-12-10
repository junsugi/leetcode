/**
 * @param {number[]} height
 * @return {number}
 */
// 풀이 확인했음
var maxArea = function(height) {
    var result = 0;
    for (var i = 0, j = height.length - 1; i < j; ) {
        result = Math.max(result, Math.min(height[i], height[j]) * (j - i));
        height[i] < height[j] ? i++ : j--;
    }
    return result;
};