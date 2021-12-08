/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var trimWord = s.trim();
    var result = "";
    for (var i = trimWord.length - 1; i >= 0; i--) {
        var temp = trimWord[i];
        if (temp !== " " && temp !== undefined) {
            result += temp;
        } else {
            return result.length;
        }
    }
    return result.length;
};