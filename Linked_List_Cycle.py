class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def has_cycle(head):
    fast = head.next.next
    slow = head
    while fast and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        index = int(input())
        llist_count = int(input())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp
            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)
        print(result)
