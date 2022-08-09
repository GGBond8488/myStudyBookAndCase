#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,l):
        # if l and l.next:
        #     cur = l
        #     curn = l.next
        #     cur.next = None
        #     while curn:
        #         tmp = curn
        #         curn = curn.next
        #         tmp.next = cur
        #         cur = tmp
        #     return cur
        # else:
        #     return l
        return l

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        print(l1.val,l2.val)
        ret = l1
        cur = l1
        print(ret.val,cur.val)
        ad = 0
        while True:
            if l1 and l2:
                add = l1.val+l2.val+ad
                l1.val = add%10
                ad = add//10
                cur = l1
                l1 = l1.next
                l2 = l2.next
                continue
            if not l1 and not l2:
                if ad>0:
                    cur.next = ListNode(ad,None)
                    cur = cur.next
                break
            if not l1:
                cur.next = l2
                break
            if not l2:
                print("enter l1")
                break

        if not cur.next:
            return self.reverse(ret)

        while True:
            if not cur.next and ad>0:
                cur.next = ListNode(ad,None)
                break
            if (cur.next.val+ad)//10==0:
                cur.next.val=cur.next.val+ad
                break
            else:
                add = cur.next.val+ad
                ad = add//10
                cur.next.val=add%10
                cur = cur.next
        return self.reverse(ret)


        
# @lc code=end
l1 = ListNode(2,None)
l1.next = ListNode(4,None)
l1.next.next = ListNode(3,None)
l2 = ListNode(5,None)
l2.next = ListNode(6,None)
l2.next.next = ListNode(4,None)

sol = Solution()
ret = sol.addTwoNumbers(l1,l2)
print(ret.val)