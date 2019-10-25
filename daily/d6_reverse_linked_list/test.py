import unittest

from daily.d6_reverse_linked_list.solution import ListNode, reverse_iterative, reverse_recursive


class MyTestCase(unittest.TestCase):
    def test_iterative(self):
        head = self._get_test_list()
        new_head = reverse_iterative(head)
        self.assertEqual('0 1 2 3 4 ', str(new_head))

    def test_recursive(self):
        head = self._get_test_list()
        new_head = reverse_recursive(head)
        self.assertEqual('0 1 2 3 4 ', str(new_head))

    @staticmethod
    def _get_test_list():
        head = ListNode(4)
        head.next = ListNode(3)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)
        head.next.next.next.next = tail = ListNode(0)

        return head


if __name__ == '__main__':
    unittest.main()
