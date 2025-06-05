# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 虚拟头节点
        dummy = ListNode()
        dummy.next = head
        # 先用双指针找到倒数第n+1个节点
        p1 = dummy
        for i in range(n+1):
            p1 = p1.next
        p2 = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
        # 找到后把倒数第n+1个节点直接指向倒数第n-1个节点 于是就删除了倒数第n个节点
        p2.next = p2.next.next
        return dummy.next
