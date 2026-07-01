class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # stores number -> index

        for i, n in enumerate(nums): # enumerate() gives both the index and the value
            diff = target - n # calculates the number needed to reach the target
            if diff in prevMap: # Is 4(7 - 3) in the dictionary?
                return [prevMap[diff], i] 
            prevMap[n] = i # store the current number
        return []  
         