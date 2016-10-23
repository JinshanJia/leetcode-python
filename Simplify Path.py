__author__ = 'Jia'
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        list = []
        startIndex = 0
        while startIndex < len(path):
            tmp = self.getBetweenSlash(path, startIndex)
            if tmp is None:
                break
            if tmp[0] == '..':
                if len(list) != 0:
                    list.pop()
            elif tmp[0] != '.':
                list.append(tmp[0])
            startIndex = tmp[1]
        if len(list) == 0:
            return '/'
        result = ''
        for s in list:
            result += '/' + s
        return result

    def getBetweenSlash(self, path, startIndex):
        while startIndex < len(path) and path[startIndex] == '/':
            startIndex += 1
        if startIndex >= len(path):
            return None
        endIndex = startIndex + 1
        while endIndex < len(path) and path[endIndex] != '/':
            endIndex += 1
        return path[startIndex:endIndex], endIndex + 1

s = Solution()
print s.simplifyPath("/./home//ap/../././././././/../..")