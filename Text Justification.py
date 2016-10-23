__author__ = 'Jia'
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left
and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
'''
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        currIndex = 0
        result = []
        while currIndex < len(words):
            count = self.canHandleWords(words, L, currIndex)
            if count == 1:
                result.append(self.leftJustify(words[currIndex], L))
            else:
                result.append(self.justifyWords(words, currIndex, count, L))
            currIndex += count
        if len(result) == 0:
            return ['']
        else:
            return result

    def canHandleWords(self, words, L, startIndex):
        length = L - len(words[startIndex])
        count = 1
        index = startIndex + 1
        while index < len(words) and length >= len(words[index]) + 1:
            count += 1
            length -= len(words[index]) + 1
            index += 1
        return count

    def justifyWords(self, words, startIndex, count, L):
        if startIndex + count >= len(words):
            length = L - len(words[startIndex])
            result = [words[startIndex]]
            count -= 1
            startIndex += 1
            while count > 0:
                result.append(" ")
                result.append(words[startIndex])
                length -= len(words[startIndex]) + 1
                startIndex += 1
                count -= 1
            result.append(' ' * length)
            return ''.join(result)
        tmp = 0
        for w in words[startIndex:startIndex + count]:
            tmp += len(w)
        aver = (L - tmp) / (count - 1)
        remaining = L - tmp - aver * (count - 1)
        result = [words[startIndex]]
        count -= 1
        startIndex += 1
        while count > 0:
            if remaining > 0:
                remaining -= 1
                result.append(" " * (aver + 1))
            else:
                result.append(" " * aver)
            result.append(words[startIndex])
            startIndex += 1
            count -= 1
        return ''.join(result)

    def leftJustify(self, word, L):
        result = [word]
        result.append(' ' * (L - len(word)))
        return ''.join(result)

s = Solution()
words = [
"This", "is", "an", "example", "of", "text", "justa.", "te"
]
l = s.fullJustify(words, 16)
for i in l:
    print i