from typing import List
# Brute force 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

# One pass Hashtable - Building and checking

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for curr in range(len(nums)):
            #curr+lookup=target
            #lookup=target-curr (if lookup exists, then return)
            if (target - nums[curr]) in lookup:
                return [curr, lookup[target - nums[curr]]]
            lookup[nums[curr]]=curr
        return list()

# Two pass - Build and then check

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

             







        

