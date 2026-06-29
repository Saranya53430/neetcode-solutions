class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set() #set stores only unique values
        for num in nums: #This visits every element in the list one by one
            if num in arr: #Check if Number Already Exists
                return True
            arr.add(num) #Add Number to Set
        return False