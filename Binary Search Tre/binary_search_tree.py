
class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def find_node(self, data):

        if data < self.data:
            if self.left is None:
                print(f"{data} is not found")
                return
            
            return self.left.find_node(data)
        
        elif data > self.data:
            if self.right is None:
                print(f"{data} is not found")
                return 
            return self.right.find_node(data)
        
        else:
            print(f"{data} is found")

    def delete(self, key):

        if key == self.data:
            
            if self.left is not None and self.right is not None:

                [pasuccessor, successor] = self.right.__sub_tree_min(self)
                

                if pasuccessor.left == successor:
                    pasuccessor.left = successor.right
                
                elif pasuccessor.right == successor:
                    pasuccessor.right = successor.left
                
                successor.left = self.left
                successor.right = self.right

                return successor
            
            else:

                if self.left is not None:
                    return self.left

                elif self.right is not None:
                    return self.right

              

        elif key < self.data:
            if self.left is not None:
                self.left = self.left.delete(key)
            
        elif key > self.data:
            if self.right is not None:
                self.right = self.right.delete(key)

        return self


    def __sub_tree_min(self, parent):

        if self.left is not None:
            return self.left.__sub_tree_min(parent)
        
        return [parent, self]



    def insert(self, data):

        if self.data:

            if data < self.data:

                if self.left is None:
                    self.left = BinarySearchTree(data)

                else:
                    self.left.insert(data)
                
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data
       
    def print_tree(self):

        if self.left:
            self.left.print_tree()
        
        print(self.data)

        if self.right:
            self.right.print_tree()

    # def max_data(self):

    #     while self.right is not None:
    #         self.right = self.max_data()
            
            
    #     return self.right.data

    # def min_data(self):

    #     while self.left is not None:
    #         self.left = self.min_data()
            
    #     return self.left.data


binary_search = BinarySearchTree(17)
binary_search.insert(12)
binary_search.insert(200)
binary_search.insert(190)
binary_search.insert(213)
binary_search.insert(56)
binary_search.insert(24)
binary_search.insert(18)
binary_search.insert(27)
binary_search.insert(28)
binary_search.insert(1)
binary_search.insert(187)

binary_search.print_tree()
# print(f"max {binary_search.max_data()}")
# print(f"min {binary_search.min_data()}")
binary_search.find_node(999)
binary_search.find_node(56)
binary_search.find_node(99)
binary_search.find_node(1)
print("after finding")
binary_search.print_tree()
# print(f"max {binary_search.max_data()}")
# print(f"min {binary_search.min_data()}")
binary_search.print_tree()
print("inserting")
binary_search.insert(1984)
print("changed max")
binary_search.print_tree()
binary_search.insert(-10)
# print(f"max {binary_search.max_data()}")
print("changed min")
binary_search.print_tree()
# print(f"min {binary_search.min_data()}")
print("after inserting")
binary_search.print_tree()
binary_search.delete(28)
print("after deleted")
binary_search.print_tree()