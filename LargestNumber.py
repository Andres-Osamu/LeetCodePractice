#https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2025-02-14
#


class Solution(object):


    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """ 
        pointerMax = None

        output = None

        while  len(nums) != 0:
            for number in nums:
                if pointerMax == None:
                    pointerMax = number
                    continue
                digitCurrent = len(str(number))
                digitMax = len(str(pointerMax))

                lowestDigit = min(digitCurrent,digitMax)

                tempCurrent = int(str(number)[:lowestDigit])
                tempMax = int(str(pointerMax)[:lowestDigit])

                if tempCurrent < tempMax:
                    continue
                elif tempCurrent > tempMax:
                    pointerMax = number
                elif tempCurrent == tempMax:
                    maxNumber = max(number, pointerMax)
                    minNumber = min(number, pointerMax)

                    if int(str(maxNumber)[lowestDigit]) > int(str(minNumber)[0]):
                        pointerMax = maxNumber

                    # if pointerMax > number:
                    #     pointerMax = number

            nums.remove(pointerMax)

            if output == None:
                output = str(pointerMax)
            else:
                output = output + str(pointerMax)
            
            pointerMax = None

        return output
            


       
            


 




nums = [3,30,34,5,9]
# nums = [10,2]
obj = Solution()
print(obj.largestNumber(nums))