class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for k in range(len(nums)):
            diff[target-nums[k]] = k
        for j in range(len(nums)):
            if nums[j] in diff:
                if j != diff[nums[j]]:
                    return [j,diff[nums[j]]]