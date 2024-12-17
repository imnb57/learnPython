### Using iteration O(n^2) time
def function():
    target = 9
    nums = [2,7,11,15]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[i+1]==target:
               return [i,j]
    return[]
result = function()
print(result)

### Using hashmap in O(n) time

def two_sum(nums, target):
    # Create a dictionary to store numbers and their indices
    seen = {}
    for i, num in enumerate(nums):
        # Calculate the complement that would add up to the target
        complement = target - num
        # Check if the complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]  # Return the indices of the two numbers
        # Otherwise, add the current number to the dictionary
        seen[num] = i
    return []  # Return an empty list if no solution is found

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


  
    

