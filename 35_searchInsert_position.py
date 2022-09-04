class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left,right = 0 , len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid +1
            else:
                right = mid - 1
        return left


ob = Solution()
print(ob.searchInsert([1,2,3],5))

