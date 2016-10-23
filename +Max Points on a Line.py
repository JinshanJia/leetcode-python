__author__ = 'Jia'
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        result = 0
        for i1 in range(len(points)):
            same = 1
            pointMax = 0
            lines = {}
            for i2 in range(i1 + 1, len(points)):
                line = self.getLine(points[i1], points[i2])
                if line is None:
                    same += 1
                    continue
                if line in lines:
                    lines[line] += 1
                else:
                    lines[line] = 1
                pointMax = max(pointMax, lines[line])
            result = max(result, pointMax + same)
        return result

    def getLine(self, point1, point2):
        A = point1.y - point2.y
        B = point2.x - point1.x
        g = self.gcd(A, B)
        if g == 0:
            return None
        A /= g
        B /= g
        return str(A) + '-' + str(B)

    def gcd(self, a, b):
        if a == 0:
            return b
        return a / abs(a) * self.gcd(abs(b % a), abs(a))