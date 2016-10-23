__author__ = 'Jia'
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
'''
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        indexK = -1
        index = 0
        while index < len(num) - 1:
            if num[index] < num[index + 1]:
                indexK = index
            index += 1
        if indexK == -1:
            num.sort()
            return num
        index = 0
        indexI = -1
        while index < len(num):
            if num[index] > num[indexK]:
                indexI = index
            index += 1
        self.swap(num, indexK, indexI)

        length = (len(num) - indexK - 1) / 2
        for i in range(length):
            self.swap(num, indexK + 1 + i, -i - 1)
        return num

    def swap(self, num, a, b):
        tmp = num[a]
        num[a] = num[b]
        num[b] = tmp

num = [3, 2, 1]
s = Solution()
tmp = list(num)
while True:
    tmp = s.nextPermutation(tmp)
    if tmp == num:
        break
    print tmp