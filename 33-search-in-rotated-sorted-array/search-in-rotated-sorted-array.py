class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        target_position = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                target_position = mid
                break
            
            if nums[mid] < nums[right]: #[1,2,3,4,5]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: #nums[mid] >= nums[right] #[7,8,9,1,2]
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return target_position
            



        