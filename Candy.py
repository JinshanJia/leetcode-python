__author__ = 'Jia'
'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        # only care that left[i] should be larger than left[i - 1] if rates[i] > rates[i - 1]
        left = [1 for i in range(len(ratings))]
        # only care that right[i] should be larger than right[i + 1] if rate[i] > rates[i + 1]
        right = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        result = 0
        for i in range(len(ratings)):
            result += max(left[i], right[i])
        return result
