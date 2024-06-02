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

def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

def remove_linkedlist(head, val):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next is not None:
        if current.next.data == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next

if __name__ == '__main__':
    llist_count = int(input("Enter the number of nodes in the linked list: "))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter node value: "))
        llist.insert_node(llist_item)

    print("Original linked list:")
    printLinkedList(llist.head)

    val_to_remove = int(input("Enter the value to remove: "))
    llist.head = remove_linkedlist(llist.head, val_to_remove)

    print("Linked list after removal:")
    printLinkedList(llist.head)





"""=========================================================Another Way============================================================="""





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

def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

def remove_linkedlist(head, val):
    # Remove all occurrences of the value from the head of the list
    while head is not None and head.data == val:
        head = head.next
    
    # Initialize current to the head of the list
    current = head
    
    # Traverse the list and remove nodes with the specified value
    while current is not None and current.next is not None:
        if current.next.data == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

if __name__ == '__main__':
    llist_count = int(input("Enter the number of nodes in the linked list: "))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter node value: "))
        llist.insert_node(llist_item)

    print("Original linked list:")
    printLinkedList(llist.head)

    val_to_remove = int(input("Enter the value to remove: "))
    llist.head = remove_linkedlist(llist.head, val_to_remove)

    print("Linked list after removal:")
    printLinkedList(llist.head)





