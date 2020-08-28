

class Node():

    def __init__(self, data):

        self.data = data
        self.next_node = None
        self.prev_node = None

def delete_node(root: Node, data) -> Node:

    if(root.data == data): #delete root

        new_root = root.next_node
        print(f"root, which is {root.data}, is deleted")
        del root
        return new_root

    iter = root
    while iter.next_node != None and iter.next_node.data != data:
        iter = iter.next_node

    if(iter.next_node == None):
        print(f'silmek istediginiz {data} elemani listede yok')
        return root

    
    be_deleted = iter.next_node
    iter.next_node = iter.next_node.next_node
    if iter.next_node != None:
        iter.next_node.prev_node = iter
        print(f"next of previous of deleted is {be_deleted.prev_node.next_node.data}")

    print(f"deleted node is {be_deleted.data}")
    print(f"previous of deleted is {be_deleted.prev_node.data}")
    
    del be_deleted
    return root

def get_linked_list(root: Node):
    iter = root
    counter = 1
    while iter != None:
        print(f"{counter}. node data: {iter.data}")
        iter = iter.next_node
        counter += 1


def add_node_inorder(root: Node, data):

    iter = root
    if root == None:
        root = Node(data)
        return root
    
    elif root.data > data: 

        new_root = Node(data)
        new_root.next_node = root 
        root.prev_node = new_root
        return new_root
    
    while iter.next_node != None and iter.next_node.data < data: 
        iter = iter.next_node
    
    node = Node(data)
    
   
    node.next_node = iter.next_node
    node.prev_node = iter
    iter.next_node = node
    if node.next_node != None:
        node.next_node.prev_node = node
       
    return root

root = Node(1)
node1 = Node(7)
node2 = Node(19)
node3 = Node(23)


root.next_node = node1
node1.prev_node = root
node1.next_node = node2
node2.prev_node = node1
node2.next_node = node3
node3.prev_node = node2

root = add_node_inorder(root, 87)
root = add_node_inorder(root, 0)
root = add_node_inorder(root, 49)
print('before deleting')
get_linked_list(root)
root = delete_node(root, 0)
root = delete_node(root, 23)
root = delete_node(root, 87)
get_linked_list(root=root)
