class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for ast in asteroids:
            alive = True
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) < stack[-1]:
                    alive = False
                    break
                elif abs(ast) > stack[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(ast)
        return stack


obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))
