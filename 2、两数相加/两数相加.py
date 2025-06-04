# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1,list2=l1,l2
        num1,num2=[],[]
        while list1:
            num1.append(str(list1.val))
            list1=list1.next
        while list2:
            num2.append(str(list2.val))
            list2=list2.next
        num1.reverse()
        num2.reverse()
        num1=''.join(num1)
        num2=''.join(num2)
        num=str(int(num1)+int(num2))
        numlist=[int(i) for i in num]
        out=ListNode(numlist[0])
        for x in numlist[1:]:
            middle=ListNode(x)
            middle.next=out
            out=middle
        return out
