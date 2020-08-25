class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums.sort()
        for n in range(len(nums)-1):
            if nums[n] == nums[n+1]:
                return True
        return False