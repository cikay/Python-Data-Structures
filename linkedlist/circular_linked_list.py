

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

def add_node_end(root: Node, data):

    if(root==None):
        root = Node(data)
        root.next_node = root
        
    
    iter = root
    while iter.next_node != root:
        iter = iter.next_node
    

    node = Node(data)
    iter.next_node = node 
    node.next_node = root
    

def delete_node(root: Node, data):

    iter = root

    if root.data == data:

        new_root = root.next_node

        while iter.next_node != root:
            iter = iter.next_node
        
        iter.next_node = new_root
        print(f"{root.data} root node deleted, root next node become root")
        del root
        return new_root
    
    while iter.next_node.data != data and iter.next_node != root:
        iter = iter.next_node
    
    if iter.next_node == root:
        print(f"list does not have {data} node")
        return root
    
    be_deleted = iter.next_node
    iter.next_node = iter.next_node.next_node
    del be_deleted
    print(f" {data} node deleted")
    return root






def get_circular_list(root: Node):

  
    print(f" {root.data}")
    iter = root.next_node
    while(iter != root):
        print(f" {iter.data}")
        iter = iter.next_node
    
def add_node_inorder(root, data):

    iter = root 
    if root ==  None:
        root = Node(data)
        return root

    elif data < root.data: 
       
        new_root = Node(data)
        new_root.next_node = root

        while iter.next_node != root:
            iter = iter.next_node

        iter.next_node = new_root
        return new_root

    while data > iter.next_node.data and iter.next_node != root:
        iter = iter.next_node
    
    node = Node(data)
    node.next_node = iter.next_node
    iter.next_node = node
    return root


root = Node(2)
node1 = Node(8)
node2 = Node(20)
node3 = Node(40)

root.next_node = node1
node1.next_node = node2
node2.next_node = node3
node3.next_node = root

get_circular_list(root)
add_node_end(root, 10)
print('added a new node to the end circular link list')
get_circular_list(root)
root = add_node_inorder(root, 1)
root = add_node_inorder(root, 17)
root = add_node_inorder(root, 190)
print('added a three node to the circular link list in order')
get_circular_list(root)
root = delete_node(root, 1)
root = delete_node(root, 17)
root = delete_node(root, 190)
root = delete_node(root, 1000)
get_circular_list(root)



