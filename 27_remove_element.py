class Solution:
    def removeElements(self,num:list[int],val:int)->int:
        for i in range(len(num)):
            if num[i]==val:
                num.remove(num)
        return num

ob = Solution()
print(ob.removeElements([3,2,2,3],3))
