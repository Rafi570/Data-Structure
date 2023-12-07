class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    # Creating an instance of Queue
    my_queue = Queue()

    # Enqueuing elements
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    # Checking the front of the queue
    print("Front of the queue:", my_queue.front())

    # Dequeuing elements
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)

    # Checking if the queue is empty
    print("Is the queue empty?", my_queue.is_empty())

    # Checking the size of the queue
    print("Size of the queue:", my_queue.size())
