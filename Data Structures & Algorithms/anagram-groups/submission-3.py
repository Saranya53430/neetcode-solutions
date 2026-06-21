class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a....z

            for c in s:
                count[ord(c) - ord('a')] += 1 # a = 80-80, b = 81-80

            res[tuple(count)].append(s) # convert the count array to a tuple and append the string to the list

        return list(res.values()) # return all the lists stored in the hash map