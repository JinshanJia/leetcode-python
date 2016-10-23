__author__ = 'Jia'
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        redP = 0
        blueP = len(A) - 1
        currP = 0
        while currP <= blueP:
            if A[currP] == 0:
                self.swap(A, redP, currP)
                redP += 1
                currP += 1
            elif A[currP] == 2:
                self.swap(A, blueP, currP)
                blueP -= 1
            else:
                currP += 1

    def swap(self, A, index1, index2):
        if index1 == index2:
            return
        tmp = A[index1]
        A[index1] = A[index2]
        A[index2] = tmp