/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    let result = "";
    for (let i = 0; i < words.length; i++) {
        let temp = "";
        for (let j = words[i].length - 1; j >= 0; j--) {
            temp += words[i][j];
        }
        if (temp === words[i]) {
            result = words[i];
            break;
        }
    }
    return result;
};