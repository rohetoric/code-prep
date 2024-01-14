class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 1
        min_product = 1
        result_product = nums[0]

        for num in nums:
            product_values = (num , num*max_product, num*min_product)
            max_product = max(product_values)
            min_product = min(product_values)

            result_product = max(result_product, max_product)
        
        return result_product

        