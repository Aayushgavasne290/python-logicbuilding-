class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
class priorityQueue:
    def __init__(self):
        self.head = None
        self.rear = None
    def enqueue(self,new_node):
        if self.head==None:
            self.head = new_node
            return
        if self.head.priority>new_node.priority:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            temp = self.head
            while temp:
                if new_node.priority<temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next
            prev.next = new_node
            new_node.next = temp
    def display(self):
        if self.head==None:
            print("Queue is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
pq = priorityQueue()
pq.enqueue(node(10,2))
pq.enqueue(node(20,1))
pq.enqueue(node(30,3))
pq.display()