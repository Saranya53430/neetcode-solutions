class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # traversing i throough the array
           for j in range(i+1, len(nums)): #traversing j except first element in array
              if nums[i] + nums[j] == target:
                return [i,j]