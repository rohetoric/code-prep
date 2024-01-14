class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_count = {}

        for num in nums:
            count_result = element_count.get(num,0) + 1
            element_count[num] = count_result
            if count_result > 1:
                return True
        
        return False

        

        