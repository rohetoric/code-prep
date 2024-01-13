class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_index_map = {}
        for i in range(len(nums)):
            element_index_map[nums[i]] = i

        for i in range(len(nums)):
            difference_position = element_index_map.get((target - nums[i]), None)
            if not difference_position:
                continue
            if difference_position == i:
                continue
            else:
                break
        
        return [i, difference_position]


            



        
        