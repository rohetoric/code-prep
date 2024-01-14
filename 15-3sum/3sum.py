class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(0,len(nums) - 2):
            first_num = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                second_num = nums[j]
                third_num = nums[k]
                
                potential_sum = first_num + second_num + third_num

                if potential_sum > 0:
                    k = k - 1
                elif potential_sum < 0:
                    j = j + 1
                else:
                    triplets.add((first_num, second_num, third_num))
                    j = j + 1
                    k = k - 1
        return triplets






        