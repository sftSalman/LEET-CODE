# this is bubble sort



nums = [2,0,2,1,1,0]
def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=temp


bubble_sort(nums)
print(nums)




