

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


    def add_inorder(self, data):

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


    def delete(self, data) -> Node:
        if self.head.data == data: #delete root
            self.head = self.head.next_node
            return

        current = self.head
        while True:
            if not current.next_node:
                print(f'Node for {data} not found to be deleted')
                break

            if current.next_node is not None and current.next_node.data == data:
                current.next_node = current.next_node.next_node
                break

            current = current.next_node



root = Node(2)
linked_list = LinkedList(root)
linked_list.add_node_to_end(789)
linked_list.get_linked_list()
linked_list.add_inorder(100)
linked_list.add_inorder(10)
linked_list.add_inorder(5)
linked_list.add_inorder(50)
linked_list.add_inorder(700)
linked_list.delete(5)
linked_list.delete(5)
linked_list.delete(700)
linked_list.delete(50)
linked_list.delete(502)
