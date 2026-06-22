class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # stores number -> frequency
        freq = [[] for i in range(len(nums) + 1)] # create buckets ( length = 6 + 1 = 7 freq(0 - 6))

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Count Frequencies(1:1,1:2,1:3)

        for n, c in count.items():
            freq[c].append(n) # Place Numbers into Buckets

        res = [] # Create Result List
        for i in range(len(freq) - 1, 0 , -1): # Traverse Buckets Backward to find highest freqs first
            for n in freq[i]:
                res.append(n) # add num to result
                if len(res) == k: 
                    return res