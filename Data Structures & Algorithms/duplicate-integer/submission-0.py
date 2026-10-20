class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_non_dup = set()
        for num in nums:
            if num in set_of_non_dup:
                return True
            else:
                set_of_non_dup.add(num)
        return False
        