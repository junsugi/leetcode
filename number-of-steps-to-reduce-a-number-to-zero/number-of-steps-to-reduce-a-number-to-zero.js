/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let count = 0;
    let result = num;
    while(result !== 0) {
        if (result % 2 === 0) {
            result /= 2;
            count++;
        } else {
            result -= 1;
            count++;
        }
    }
    return count;
};