__author__ = 'Jia'
'''
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such
that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections
import sets
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        resultDict = {}
        dict.add(end)
        dict.add(start)
        recorder = [sets.Set(), sets.Set()]
        currentLevel = 0
        preLevel = 1
        recorder[currentLevel].add(start)

        while len(recorder[currentLevel]) != 0 and end not in recorder[currentLevel]:
            recorder[preLevel].clear()
            preLevel = currentLevel
            currentLevel = (currentLevel + 1) % 2
            for s in recorder[preLevel]:
                dict.remove(s)
            for word in recorder[preLevel]:
                chars = list(word)
                for i in range(len(chars)):
                    head = ''.join(chars[:i])
                    tail = ''.join(chars[i + 1:])
                    for i in range(ord('a'), ord('z') + 1):
                        tmp = head + chr(i) + tail
                        if tmp in dict:
                            recorder[currentLevel].add(tmp)
                            if tmp in resultDict:
                                resultDict[tmp].add(word)
                            else:
                                resultDict[tmp] = sets.Set([word])

        def generateResult(resultDict, end, start):
            queue = collections.deque([[end]])
            result = []
            while len(queue) != 0:
                path = queue.popleft()
                # print "*******"
                # print path
                # print queue
                # print "#######"
                for string in resultDict[path[0]]:
                    tmp = [string]
                    tmp.extend(path)
                    if string == start:
                        result.append(tmp)
                    else:
                        queue.append(tmp)
            return result
        if end not in resultDict:
            return []
        print resultDict
        return generateResult(resultDict, end, start)

    def findLadders2(self, start, end, dict):
        resultDict = {}
        dict.add(start)
        dict.add(end)
        toSearch = sets.Set([start])
        while len(toSearch) != 0 and end not in toSearch:
            for word in toSearch:
                dict.remove(word)
            nextToSearch = sets.Set()
            for word in toSearch:
                chars = list(word)
                for i in range(len(chars)):
                    head = ''.join(chars[:i])
                    tail = ''.join(chars[i + 1:])
                    for i in range(ord('a'), ord('z') + 1):
                        tmp = head + chr(i) + tail
                        if tmp in dict:
                            if tmp in resultDict:
                                resultDict[tmp].add(word)
                            else:
                                resultDict[tmp] = sets.Set([word])
                            nextToSearch.add(tmp)
            toSearch = nextToSearch

        def generateResult(resultDict, end, start):
            queue = collections.deque([[end]])
            result = []
            while len(queue) != 0:
                path = queue.popleft()
                for string in resultDict[path[0]]:
                    tmp = [string]
                    tmp.extend(path)
                    if string == start:
                        result.append(tmp)
                    else:
                        queue.append(tmp)
            return result
        if end not in resultDict:
            return []
        return generateResult(resultDict, end, start)


s = Solution()
start = "hit"
end = "cog"
dict = sets.Set(["hot","dot","dog","lot","log"])
l = s.findLadders2(start, end, dict)
for i in l:
    print i