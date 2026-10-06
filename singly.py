# singly linked list


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


list = linkedlist()

n1 = node(1)
n2 = node(20)
n3 = node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.print()