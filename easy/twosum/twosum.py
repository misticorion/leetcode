# https://leetcode.com/problems/two-sum/
# Runtime: 96 ms
# Memory Usage: 15.4 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
          The dictionary called `twoSumDict` will be used to store the indices of the numbers in `nums`.
          The method iterates over the list `nums`. For each number in `nums`, the method does the following:
          * Calculates the difference between the number and `target`.
          * Checks if the difference is in `twoSumDict`. If it is, the method returns a list containing the index of the current number and the index of the number in `twoSumDict` that corresponds to the difference.
          * Adds the current number to `twoSumDict`. This is done so that the difference between the current number and `target` can be looked up later.

        """
        twoSumDict = {}

        for i in range(0, len(nums)):

            difference = target - nums[i]

            if difference in twoSumDict:
                return [i, twoSumDict[difference]]

            twoSumDict[nums[i]] = i

            
