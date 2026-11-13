class Solution:
    def three_sum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result


obj = Solution()
print(obj.three_sum([-1, 0, 1, 2, -1, -4]))
