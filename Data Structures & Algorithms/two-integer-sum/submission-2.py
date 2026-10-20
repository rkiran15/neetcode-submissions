class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff in track and track[diff] != k:
                return [track[diff],k]
            track[v] = k
