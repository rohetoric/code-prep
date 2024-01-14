class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num

            if maxSum < currentSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
                
        return maxSum
        