#O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht ={} 
        for i,n in enumerate(nums):
            val = target - n
            if val in ht:
                return [ht[val],i]
            ht[n]=i

#bruteforce O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return[i,j]

