#https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2025-02-14
#


class Solution(object):

    # This function will reversively call itself to continuously break down the number until it reaches a digit 
    # subset that is comparably different

    def findLargestNumber(self, numA, numB):


        # subsetA = int(str(numA)[lowestDigit:])
        digitA = len(str(numA))
        digitB = len(str(numB))

        lowestDigit = min(digitA,digitB)

        tempA = int(str(numA)[:lowestDigit])
        tempB = int(str(numB)[:lowestDigit])

        if tempA < tempB:
            return numB
        elif tempA > tempB:
            return numA
        else: # tempA == tempB:
            maxNumber = max(numA, numB)
            minNumber = min(numA, numB)
            # Whenever a tiebreaker is met i.e. 3 vs 3 (original 3 vs 33)
            # Then pick the bigger number, it doesnt matter as no number can exist such that
            # placing it inbetween the two will result in different value
            # If the number is < 3 then it will always be after 3+33+_
            # If the number is > 3 then it will always be before _+3+33
            if lowestDigit == len(str(maxNumber)):
                print()
                return  maxNumber
            # temp = str(maxNumber)[lowestDigit:]
            # if temp == '':
            #     print()
            # subsetMaxNumber = int(temp)
            subsetMaxNumber = int(str(maxNumber)[lowestDigit:])

            result = self.findLargestNumber(subsetMaxNumber, minNumber)

            if result == subsetMaxNumber:
                return maxNumber
            else:
                return minNumber

            # return 


    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """ 
        pointerMax = None

        output = None

        while  len(nums) != 0:

            # The idea is to take the first X digits (left to right) and choose whichever one has the highest value
            # e.g. 543 vs 34509 = 534 > 345

            

            for number in nums:
                if pointerMax == None:
                    pointerMax = number
                    continue
                # Issues when duplicate numbers were found (this prevents the subset issue of just wiping the number)
                if number == pointerMax:
                    continue
                else:
                    pointerMax = self.findLargestNumber(pointerMax, number)

            nums.remove(pointerMax)

            if output == None:
                output = str(pointerMax)
            else:
                output = output + str(pointerMax)
            
            pointerMax = None

        #  Removes left zeroes
        return str(int(str(output)))

    
            


       
            

 
# product = 1113 - 11
# 11  1113
# 11 13

# 111311 x 1113



# 11 x 1113
# 11 x 11
# 11 x 13
# 13

# nums = [3,30,34,5,9]
# nums =  [111311,1113]

# 31 x 311
nums = [3,43,48,94,85,33,64,32,63,66]

# [10, 2, 45]
# _ _ _ _ _
# 99999
# 1 0
obj = Solution()
print(obj.largestNumber(nums))





# def largestNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: str
    #     """ 
    #     pointerMax = None

    #     output = None

    #     while  len(nums) != 0:

    #         # The idea is to take the first X digits (left to right) and choose whichever one has the highest value
    #         # e.g. 543 vs 34509 = 534 > 345

    #         for number in nums:
    #             if pointerMax == None:
    #                 pointerMax = number
    #                 continue
    #             digitCurrent = len(str(number))
    #             digitMax = len(str(pointerMax))

    #             lowestDigit = min(digitCurrent,digitMax)

    #             tempCurrent = int(str(number)[:lowestDigit])
    #             tempMax = int(str(pointerMax)[:lowestDigit])

    #             if tempCurrent < tempMax:
    #                 continue
    #             elif tempCurrent > tempMax:
    #                 pointerMax = number


    #             # Change this [432,432431] delete the common subset of the largest number then 
    #             # compare the remainder with the original smaller number
    #             elif tempCurrent == tempMax:
    #                 maxNumber = max(number, pointerMax)
    #                 minNumber = min(number, pointerMax)

    #                 if int(str(maxNumber)[lowestDigit]) > int(str(minNumber)[0]):
    #                     pointerMax = maxNumber
                    
    #                 elif int(str(maxNumber)[lowestDigit]) == int(str(minNumber)[0]):
    #                     subMaxNumber = int(str(maxNumber)[lowestDigit:])

    #                     tempLowestDigit = min (subMaxNumber, minNumber)



    #                 # if pointerMax > number:
    #                 #     pointerMax = number

    #         nums.remove(pointerMax)

    #         if output == None:
    #             output = str(pointerMax)
    #         else:
    #             output = output + str(pointerMax)
            
    #         pointerMax = None

    #     return output