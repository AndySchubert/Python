# the ^ operator stands for the XOR operator which stands for exclusive or and is a binary toggle.

class Solution:
    def singleNumber(nums):
        result = 0
        for n in nums:
            result ^= n
        return result

array = [0, 2, 4, 5, 7, 1, 1, 5, 4, 2, 0]

print(Solution.singleNumber(array))