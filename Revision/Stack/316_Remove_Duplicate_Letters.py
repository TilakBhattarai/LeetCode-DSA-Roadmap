class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        stack = []

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in s:

            freq[char] -= 1

            if char in stack:
                continue

            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return "".join(stack)


obj = Solution()
print(obj.removeDuplicateLetters("cbacdcbc"))
