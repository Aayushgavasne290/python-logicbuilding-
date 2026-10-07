# singly linear linked list
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

    def insert(self, new_node, pos):
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while p < pos and temp is not None and temp.next is not None:
            temp = temp.next
            p += 1

        if temp is None:

            
            return

        new_node.next = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # def print(self):
    #     temp = self.head
    #     sum=0
    #     count=0
    #     while temp:
    #         if temp.data > 0:
    #             print(temp.data)
    #         sum = sum + temp.data
    #         count+=1 
    #         temp = temp.next
    #     print(f"Sum: {sum}, Count: {count}")

list = linkedlist()

n1 = node(10)
n2 = node(20)   
n3 = node(30)
n4 = node(40)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.insert(node(100),4)
list.insert(node(200),5)
list.print()
