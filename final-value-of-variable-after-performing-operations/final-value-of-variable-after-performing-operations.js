/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let ans = 0
    for(let i = 0; i < operations.length; i++) {
        switch(operations[i]) {
            case "--X":
                --ans;
                break;
            case "X--":
                ans--;
                break;
            case "++X":
                ++ans;
                break;
            case "X++":
                ans++;
                break;
        }
    }
    return ans;
};