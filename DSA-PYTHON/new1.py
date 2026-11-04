# # Q. 1 Create a Stack with following operations 
# # 1.	Push 
# # 2.	Pop 
# # 3.	Display 
# # 4.	Reverse String using Stack 
# # 5.	Reverse Stack using another Stack 
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# class stack:
#     def __init__(self):
#         self.top = None

#     def isempty(self):
#         return self.top is None

#     def push(self, new_node):
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.isempty():
#             print("Stack is empty")
#         else:
#             temp = self.top
#             print("Popped element: ", temp.data)
#             self.top = self.top.next



#             temp = None

#     def display(self):
#         temp = self.top
#         print("Stack elements...")
#         while temp:
#             print(temp.data)
#             temp = temp.next

#     def reverseString(self, string):
#         st1 = stack()

#         for ch in string:
#             st1.push(Node(ch))

#         result = ""
#         while not st1.isempty():
#             result = result + st1.top.data
#             st1.top = st1.top.next

#         print("Reversed String: ", result)

#     def reverse(self):
#         st1 = stack()
#         temp = self.top

#         while temp:
#             st1.push(Node(temp.data))
#             temp = temp.next

#         return st1

# st = stack()

# st.push(Node(10))
# st.push(Node(100))
# st.push(Node(45))
# st.push(Node(68))
# st.push(Node(80))

# st.display()


# st.pop()
# st.display()

# st.reverseString("abcdefghijklmnopqrstuvwxyz")

# st1 = st.reverse()
# print("Reversed Stack...")
# st1.display()

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = temp.next
        return temp.data


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def display(self):
        temp = self.front


        print("Queue elements: ", end="")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def reverse(self):
        st = stack()
        temp = self.front


        while temp:
            st.push(temp.data)
            temp = temp.next

        newQueue = Queue()

        while st.top:
            newQueue.enqueue(st.pop())

        return newQueue

    def merge(self, q2):
        q3 = Queue()

        temp = self.front
        while temp:
            q3.enqueue(temp.data)
            temp = temp.next

        temp = q2.front
        while temp:
            q3.enqueue(temp.data)
            temp = temp.next

        return q3

    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            return True

        return False



q1 = Queue()

q1.enqueue('A')
q1.enqueue('B')
q1.enqueue('C')

print("First Queue: ")
q1.display()

print("Dequeue: ", q1.dequeue())
q1.display()

q3 = q1.reverse()
print("Reversed Queue: ")
q3.display()

q2 = Queue()

q2.enqueue('D')
q2.enqueue('E')


q2.enqueue('F')

print("Second Queue: ")
q2.display()

q4 = q1.merge(q2)
print("Merged Queue: ")
q4.display()


if q1.identical(q2):
    print("Both Queues are Identical")
else:
    print("Both Queues are Not Identical")
