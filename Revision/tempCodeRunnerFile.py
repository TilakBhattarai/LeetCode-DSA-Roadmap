class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for ast in asteroids:
            print(ast)


obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))
