class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(j, end):
            while j < end:
                nums[j], nums[end] = nums[end], nums[j]
                j += 1
                end -= 1
        n = len(nums)
        if n < 2: return nums
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return reverse(0, n - 1)
        k = n - 1
        while nums[k] <= nums[i - 1]:
            k -= 1
        nums[i - 1], nums[k] = nums[k], nums[i - 1]
        reverse(i, n - 1)
        return nums