from typing import List


class ListNode:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data: int):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        return new_node

    def print_list(self):
        curr = self.head
        out: List[str] = []
        while curr is not None:
            out.append(str(curr.data))
            curr = curr.next
        print(" ".join(out))

    def delete(self, key: int):
        temp = self.head
        prev = None

        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    node = lst.append(4)

    print(lst.detect_loop())

# remove the loop ??????