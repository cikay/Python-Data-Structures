

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None



class QueueLinkedList():

    def __init__(self, data):
        self.root = Node(data)
        self.last_node = self.root

    
    def enqueue(self, data):

        if self.root == None:
            self.root = Node(data)
            return

        self.last_node.next_node = Node(data)
        self.last_node = self.last_node.next_node

    
    def dequeue(self):

        if self.root == None:
            print('linked list empty')
            return
        
        old_root = self.root
        old_root_value = self.root.data
        self.root = self.root.next_node
        del old_root
        return old_root_value

    def get_items(self):
        iter = self.root
        items = []
        while(iter != None):
            items.append(iter.data)
            iter = iter.next_node

        print(items)


qlinklist = QueueLinkedList(10)

for i in range(10):
    qlinklist.enqueue(i)
    qlinklist.get_items()

print("enqueue finished")
for i in range(13):
    qlinklist.dequeue()
    qlinklist.get_items()





