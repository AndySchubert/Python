NONE = 0b00
UP = 0b01
DOWN = 0b10

class Solution(object):
    def validMountainArray(self, array: list[int]) -> bool:
        # mountain array is an array that startw with a low value, has a peak in the middle and declines, just like a mountain
        # differentiation can be made whether it has to be strictly going up or down (what if there's the same value consecutively? e.g. [1, 2, 2, 3, 1]
        direction = NONE # state machine to indicate the direction of the array

        for i in range(0,len(array)):
            if i <= 0:
                continue

            if direction == NONE:
                if array[i] > array[i-1]:
                    direction = UP
                    continue

            if direction == UP: 
                if array[i] > array[i-1]:
                    continue
                if array[i] < array[i-1]:
                    direction = DOWN
                    continue
            
            if direction == DOWN:
                if array[i] < array[i-1]:
                    continue
            return False
        return direction == DOWN


s = Solution()
array = [1,2,3,1] # returns True
array2 = [1,2,2,3,1] # returns False

test = s.validMountainArray(array)

print(test)