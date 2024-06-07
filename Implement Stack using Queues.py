# Define the MyStack class
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:   
        return len(self.stack) == 0

# Create an object of MyStack
my_stack = MyStack()

# Push elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Get the top element
print(f"Top element: {my_stack.top()}")  # Output: Top element: 3

# Pop an element from the stack
print(f"Popped element: {my_stack.pop()}")  # Output: Popped element: 3

# Check the top element again
print(f"Top element after pop: {my_stack.top()}")  # Output: Top element after pop: 2

# Check if the stack is empty
print(f"Is the stack empty? {my_stack.empty()}")  # Output: Is the stack empty? False

# Pop all elements to empty the stack
my_stack.pop()
my_stack.pop()

# Check if the stack is empty again
print(f"Is the stack empty after popping all elements? {my_stack.empty()}")  # Output: Is the stack empty after popping all elements? True
