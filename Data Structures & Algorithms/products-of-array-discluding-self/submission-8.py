class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Create Result Array
        
        prefix = 1 # Prefix Pass, stores the product of all numbers to the left of the current index
        for i in range(len(nums)): # Traverse from left to right
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1 # Initialize postfix product
        for i in range(len(nums) - 1, -1, -1): # Traverse from right to left
            res[i] *= postfix
            postfix *= nums[i]
        return res
# First loop stores the product of all numbers on the left of each index.
# Second loop multiplies by the product of all numbers on the right of each index.