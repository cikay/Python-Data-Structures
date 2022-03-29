


class LinkedListNode:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        new_root = Node(value)
        new_root.next = self.root
        self.root = new_root


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, size) -> None:
        self.table = [LinkedListNode()]*size


    def insert(self, value):
        index = self.hash(value)
        root = self.table[index]
        root.insert(value)


    def hash(self, value):
        chars_list = list(value)
        int_list = map(lambda x: ord(x), chars_list)
        return sum(int_list) % len(self.table)


    def print_list(self, index):
        root = self.table[index].root
        current_node = root
        while True:
            if not current_node:
                break
            
            print(current_node.value)
            current_node = current_node.next


hash_table = HashTable(1000)
hash_table.insert('muzaffer')
hash_table.insert('zaffermu')
index = hash_table.hash('muzaffer')
hash_table.print_list(index)
