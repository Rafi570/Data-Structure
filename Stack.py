class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    # Creating an instance of Stack
    my_stack = Stack()

    # Pushing elements onto the stack
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    # Peeking at the top of the stack
    print("Top of the stack:", my_stack.peek())

    # Popping elements from the stack
    popped_item = my_stack.pop()
    print("Popped item:", popped_item)

    # Checking if the stack is empty
    print("Is the stack empty?", my_stack.is_empty())

    # Checking the size of the stack
    print("Size of the stack:", my_stack.size())
