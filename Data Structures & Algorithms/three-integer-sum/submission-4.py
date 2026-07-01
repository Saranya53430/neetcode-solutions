class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # stores all valid triplets
        nums.sort() # sort the array
        # Sorting is important because it allows us to use the two-pointer technique

        for i, a in enumerate(nums): # Traverse each number, i - index and a - current number
            if i > 0 and a == nums[i-1]: # skip duplicate first elements
                continue

            l, r = i + 1, len(nums) - 1 # initialize two pointers
            while l < r: # loop until pointers meet
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # skip duplicate left values
                        l += 1
        return res