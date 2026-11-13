class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []
        n = len(num)
        result = ""

        for val in num:
            while stack and k > 0 and stack[-1] > val:
                stack.pop()
                k -= 1
            stack.append(val)

        for val in num:
            while stack and k > 0:
                stack.pop()
        result = "".join(stack).lstrip("0")

        if not result:
            return "0"


obj = Solution()
print(obj.removeKdigits("10", 2))
