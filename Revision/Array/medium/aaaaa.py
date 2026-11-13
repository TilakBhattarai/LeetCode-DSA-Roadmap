# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         left = 0
#         right = n - 1

#         while left < right:
#             mid = (left + right) // 2

#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return nums[left]


# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         n = len(nums)
#         left = 0
#         right = n - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             if nums[mid] > nums[right]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1

#         if list1.val < list2.val:
#             head = list1
#             list1 = list1.next
#         else:
#             head = list2
#             list2 = list2.next

#         current = head

#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next

#             current = current.next

#         current.next = list1 if list1 else list2


# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(nums)
#         left = 0
#         right = n - 1
#         first = -1
#         second = -1

#         # left search

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 first = mid
#                 right = mid - 1

#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         left = 0
#         right = n - 1

#         # right search

#         while left <= right:
#             mid = (left + right) // 2


#             if nums[mid] == target:
#                 second = mid
#                 left = mid + 1

#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return [first, second]


# obj = Solution()
# print(obj.searchRange([5, 7, 7, 8, 10], 8))


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        product = 1
        maxProduct = float("-inf")

        for num in nums:
            product *= num
            maxProduct = max(maxProduct, product)

            if product == 0:
                product = 1
        product = 1
        for num in reversed(nums):
            product *= num
            maxProduct = max(maxProduct, product)

            if product == 0:
                product = 1

        return maxProduct


obj = Solution()
print(obj.maxProduct([2, 3, -2, 4]))
