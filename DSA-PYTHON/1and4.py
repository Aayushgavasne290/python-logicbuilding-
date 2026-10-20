class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Manages the linked list operations."""
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append)
    def append(self, data):
        """Adds a new node with data to the end of the list."""
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Attach the new node at the end
        current.next = new_node

    # 2. Traverse and Print the Node Values
    def display(self):
        """Walks through the list from head to end and prints each value."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    # 3. Insert Node at a Specific Position
    def insert_at_position(self, position, data):
        """Inserts a new node at a given 1-based position."""
        new_node = Node(data)

        # Insertion at the beginning (Position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_position = 1

        # Traverse to the node just before the target position (position - 1)
        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        # If the position is out of bounds
        if current is None:
            print(f"Position {position} is out of bounds.")
            return

        # Splice the new node into the chain
        new_node.next = current.next
        current.next = new_node

    # 4. Delete Alternate Nodes in the Linked List
    def delete_alternate_nodes(self):
        """Removes every second node starting from the first alternate."""
        if self.head is None:
            return

        current = self.head
        
        # Loop while there is a current node and a node after it to delete
        while current is not None and current.next is not None:
            # Bypass the next node
            current.next = current.next.next
            # Move current forward to the next node to keep
            current = current.next


# --- Example Usage ---
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # 1. Appending nodes
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(40)
    
    print("Initial List:")
    sll.display()  # Output: 10 -> 20 -> 30 -> 40 -> None

    # 3. Inserting a node at a specific position (e.g., insert 25 at position 3)
    sll.insert_at_position(3, 25)
    print("\nAfter Inserting 25 at Position 3:")
    sll.display()  # Output: 10 -> 20 -> 25 -> 30 -> 40 -> None

    # 4. Deleting alternate nodes
    sll.delete_alternate_nodes()
    print("\nAfter Deleting Alternate Nodes:")
    sll.display()  # Output: 10 -> 25 -> 40 -> None