class Solution(object):
    def compress(self, chars):
        arr = [chars[0]]
        freq = [1]

        for i in range(1,len(chars)):
            if chars[i] != chars[i-1]:
                arr.append(chars[i])
                freq.append(1)
            else:
                freq[-1] +=1

        result = []

        for i in range(len(arr)):
            result.append(arr[i])
            
            if freq[i] > 1:
                for digit in str(freq[i]):
                    result.append(digit)

        chars[:] = result
        return len(chars)
        