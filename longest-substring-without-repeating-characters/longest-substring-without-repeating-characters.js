/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let temp = "";
    let max = 0;
    for (let i = 0; i < s.length; i++) {
        temp += s[i];
        for (let j = i+1; j < s.length; j++) {
            if (temp.indexOf(s[j]) === -1) {
                temp += s[j];
            } else {
                break;
            }
        }
        max = temp.length > max ? temp.length : max;
        temp = "";
    }
    return max;
};