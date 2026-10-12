





# # class linkedlist:
# #     def reverse(self):   # reversing thr linkedlist
# #         self.head=prev
# #     def findmid_del(self):
# #         temp=temp1=self.head
# #         prev=None
# #         while temp1 and temp1.next:
# #             prev=temp
# #             temp=temp.next
# #             temp1=temp1.next.next
# #         print("middle node:",temp.data)
# #         prev.next=temp.next
# #         temp=None
# #     def delfirst_last(self):
# #         temp1=self.head 
# #         temp1=None
# #         prev=None
# #         temp=self.head=self.head.next
# #         while(temp.next):
# #             prev=temp
# #             temp=temp.next
# #         prev               

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     # def delete_first(self):
#     #     if self.head is None:
#     #         print("List is empty")
#     #         return

#     #     self.head = self.head.next

#     # def delete_last(self):
#     #     if self.head is None:
#     #         print("List is empty")
#     #         return

#     #     if self.head.next is None:
#     #         self.head = None
#     #         return

#     #     current = self.head

#     #     while current.next.next is not None:
#     #         current = current.next

#     #     current.next = None

   

#     # def alternate nodes in singly linkedlist
#     def alterdel(self):
#        prev=self.head
#        temp=self.head.next
#        while prev and temp:
#            prev.next=temp.next
#            temp=None
#            prev=prev.next
#            if prev:
#                temp=prev.next
#     def display(self):
#             current = self.head
    
#             while current is not None:
#                 print(current.data, end=" -> ")
#                 current = current.next
    
#             print("None")           
# ll = LinkedList()

# ll.insert(10)
# ll.insert(20)
# ll.insert(30)

# ll.display()

# # ll.delete_first()
# ll.display()

# # ll.delete_last()
# ll.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Delete alternate nodes
    def alterdel(self):
        prev = self.head

        if prev is None:
            return

        temp = prev.next

        while prev and temp:
            prev.next = temp.next
            prev = prev.next

            if prev:
                temp = prev.next

    # Display linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create linked list
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

print("Original linked list:")
ll.display()

ll.alterdel()

print("After deleting alternate nodes:")
ll.display()