

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head


    def print_list(self):
        current = self.head
        items = []
        while True:
            if current is None:
                break

            items.append(str(current.data))
            current = current.next

        print('->'.join(items))


    def add_node_inorder(self, node):
        current = self.head
        while True:
            if not current.next or current.next.data > node.data:
                current.next, node.next = node, current.next
                break

            current = current.next



    def add_to_end(self, data):
        current = self.head

        while True:
            if not current.next:
                current.next = Node(data)
                break

            current = current.next


    def add_inorder(self, data):

        current = self.head
        if data < self.head.data: #root change

            new_root = Node(data)
            new_root.next = root
            return new_root

        while current.next != None and current.next.data < data:
            current = current.next

        node = Node(data)
        node.next = current.next
        current.next = node


    def delete(self, data) -> Node:
        if self.head.data == data: #delete root
            self.head = self.head.next
            return

        current = self.head
        while True:
            if not current.next:
                print(f'Node for {data} not found to be deleted')
                break

            if current.next is not None and current.next.data == data:
                current.next = current.next.next
                break

            current = current.next



root = Node(2)
linked_list = LinkedList(root)
linked_list.add_inorder(100)
linked_list.add_inorder(10)
linked_list.add_inorder(5)
linked_list.add_inorder(50)
linked_list.add_inorder(880)
linked_list.add_inorder(700)
linked_list.add_to_end(-2)
linked_list.delete(5)
linked_list.delete(5)
linked_list.delete(700)
linked_list.delete(50)
linked_list.delete(502)
node = Node(274)
linked_list.add_node_inorder(node)
linked_list.print_list()

