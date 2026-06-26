class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cal = 0

        for i in range(len(nums) - 1) :
            for j in range(i + 1, len(nums)) :
                cal = nums[i] + nums[j]

                if cal == target :
                    return i, j