class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i in range(0,len(nums)):
            diff = target-nums[i]
            if diff in seenMap:
                return [seenMap[diff], i]
            else:
                    seenMap[nums[i]] = i
        return