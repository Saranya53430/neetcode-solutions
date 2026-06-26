class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Convert List to Set
        longest = 0 # Initialize Longest
        
        for n in nums: # Traverse Every Number
            if (n - 1) not in numSet: # check if 100 - 1 = 99 is present or not to find the beginning of the sequence
                length = 0 # Count the sequence
                while (n + length) in numSet: # 100 + 0 = 100 in numSet? 
                    length += 1 # if yes, increment 100 + 1 = 101 
                longest = max(length, longest)
        return longest