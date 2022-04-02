

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, head):
        self.head = head


    def get_linked_list(self):
        current = self.head
        counter = 1
        while True:
            if current is None:
                break

            print(f"{counter}. node data: {current.data}")
            current = current.next_node
            counter += 1


    def add_node_to_end(self, data):
        current = self.head

        while current.next_node != None:
            current = current.next_node

        current.next_node = Node(data)
        print("added new node to the linked list")


    def add_node_inorder(self, data):

        current = self.head

        if self.head is None:
            return Node(data)
        
        elif data < self.head.data: #root change

            new_root = Node(data)
            new_root.next_node = root
            return new_root

        while current.next_node != None and current.next_node.data < data:
            current = current.next_node

        node = Node(data)
        node.next_node = current.next_node
        current.next_node = node


def delete_node(root: Node, data) -> Node:

    if(root.data == data): #delete root

        new_root = root.next_node
        del root
        print('root is deleted')
        return new_root

    iter = root
    while iter.next_node != None and iter.next_node.data != data:
        iter = iter.next_node

    if(iter.next_node == None):
        print(f'silmek istediginiz {data} elemani listede yok')
        return root

    
    be_deleted = iter.next_node
    iter.next_node = iter.next_node.next_node
    del be_deleted
    return root


root = Node(2)
root = delete_node(root=root, data=5)
root = delete_node(root=root, data=5)
root = delete_node(root=root, data=700)
root = delete_node(root=root, data=50)
linked_list = LinkedList(root)
linked_list.add_node_to_end(789)
linked_list.get_linked_list()
linked_list.add_node_inorder(100)
linked_list.add_node_inorder(10)
linked_list.add_node_inorder(5)
linked_list.add_node_inorder(50)
linked_list.add_node_inorder(700)



 

    