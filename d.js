
# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

var twoSum = function(nums, target) {
    let comp = 0
    let array = []

    for(let i=0 i < nums.length i++) {
        comp = target - nums[i]
        
        if(nums.includes(comp) & & nums.indexOf(comp) !== i){
            array.push(i)
            array.push(nums.indexOf(comp))
            break;
        }
    }

    return array
    # console.log(array)
}

# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

var twoSum = function(nums, target) {
    let comp = 0
    let array = []

    for(let i=0 i < nums.length i++) {
        comp = target - nums[i]
        
        if(nums.includes(comp) & & nums.indexOf(comp) !== i){
            array.push(i)
            array.push(nums.indexOf(comp))
            break;
        }
    }

    return array
    # console.log(array)
}
