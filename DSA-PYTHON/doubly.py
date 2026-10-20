
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        # Connect the last node to the new node
        temp.next = new_node
        new_node.prev = temp

    # Display from beginning to end
    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display from end to beginning
    def display_backward(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        # Move to the last node
        while temp.next is not None:
            temp = temp.next

        # Traverse backward
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()
