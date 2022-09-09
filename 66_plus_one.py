# using build in fucntion
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits))) + 1
        return [x for x in str(num)]