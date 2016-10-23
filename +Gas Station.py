__author__ = 'Jia'
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
(i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        index = 0
        currIndex = index
        remaining = 0
        while index < len(gas):
            tmp = gas[currIndex] - cost[currIndex]
            if remaining + tmp >= 0:
                currIndex = (currIndex + 1) % len(gas)
                if currIndex == index:
                    return index
                remaining += tmp
            else:
                if currIndex < index:
                    return -1
                index = currIndex + 1
                remaining = 0
                currIndex = index
        return -1

gas = [2, 4]
cost = [3, 3]
s = Solution()
print s.canCompleteCircuit(gas, cost)