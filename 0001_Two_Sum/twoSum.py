class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, val in enumerate(nums):
            key = target - val
            if key in d:
                return [idx, d[key]]
            else:
                d[val] = idx
        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))

