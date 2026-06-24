class Solution:

    def encode(self, strs):
        res = "" # Create an empty string to store the encoded result
        for s in strs: # Loop through each string
            res += str(len(s)) + "#" + s # res = "4#neet"
        return res

    def decode(self, str):
        res = [] 
        i = 0 # points to the start of the next encoded string.
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i : j]) # Extract Length
            res.append(str[j + 1 : j + 1 + length]) # Extract String
            i = j + 1 + length
        return res