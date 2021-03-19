class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force
        -----------
        Time Complexity:    O(n^2)
        Space Complexity:   O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Table
        ---------
        Time Complexity:    O(n)
        Space Complexity:   O(n)
        """
        hashtable = dict()
        for index, item in enumerate(nums):
            if target - item in hashtable:
                return [index, hashtable[target - item]]
            hashtable[item] = index
