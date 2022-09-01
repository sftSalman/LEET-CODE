class Solution:
    def twoSum(self, nums,target):
        val_dict= {}
        for i ,n in enumerate(nums):
            diff = target-n
            if diff in val_dict:
                return [val_dict[diff],i]
            val_dict[n]=i

input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))