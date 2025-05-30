"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            complemento = target - value
            if complemento in dic:
                return [dic[complemento], index]
            dic[value] = index
        return None
    
    def TwoSumBruteForce(lista, target):
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if (lista[i] + lista[j]) == target:
                    return [i, j]
        return None