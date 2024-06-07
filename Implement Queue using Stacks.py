# Define the MyQueue class
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Create an object of MyQueue
my_queue = MyQueue()

# Push elements into the queue
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

# Get the front element
print(f"Front element: {my_queue.peek()}")  # Output: Front element: 1

# Pop an element from the queue
print(f"Popped element: {my_queue.pop()}")  # Output: Popped element: 1

# Check the front element again
print(f"Front element after pop: {my_queue.peek()}")  # Output: Front element after pop: 2

# Check if the queue is empty
print(f"Is the queue empty? {my_queue.empty()}")  # Output: Is the queue empty? False

# Pop all elements to empty the queue
my_queue.pop()
my_queue.pop()

# Check if the queue is empty again
print(f"Is the queue empty after popping all elements? {my_queue.empty()}")  # Output: Is the queue empty after popping all elements? True
