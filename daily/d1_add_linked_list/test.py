import unittest

from daily.d1_add_linked_list.solution import ListNode


class MyTestCase(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        self.assertEqual('708', str(l1.add(l2)))

    def test_2(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        self.assertEqual('705', str(l1.add(l2)))

    def test_3(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l2.next.next.next = ListNode(9)

        self.assertEqual('7059', str(l1.add(l2)))

    def test_4(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)

        l2 = ListNode(8)
        l2.next = ListNode(8)
        l2.next.next = ListNode(8)
        l2.next.next.next = ListNode(8)

        self.assertEqual('7898', str(l1.add(l2)))


if __name__ == '__main__':
    unittest.main()
