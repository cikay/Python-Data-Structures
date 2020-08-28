
import ctypes 


class DynamicArray(object):

    def __init__(self):
        self.length = 0
        self.capacity = 2
        self.array = self.make_array(self.capacity)
    

    def __len__(self):
        return self.length

    
    def getitem(self, index):
        if not 0 <= index < self.length:
    
            return IndexError('k is out of bounging')

        return self.array[index]
    
  
    def pop(self):

        if self.array == None or self.length == 0:
            print('array is empty, can not be popped')
            return 
        if self.length == 1:
            self.array = None
            self.length = 0
            self.capacity = 2
            return

        elif self.capacity/4 >= self.length: 
            self.__resize(int(self.capacity/2))
            print(f'from pop capacity is {self.capacity}')

        popped_item = self.array[self.length-1]
        self.array[self.length-1] = 0

        self.length -= 1
        return popped_item

    def push(self, item):

        if self.array == None:
            self.array = self.make_array(self.capacity)
        
        if self.length == self.capacity:

            self.__resize(2*self.capacity)
            

        self.array[self.length] = item
        self.length += 1
    
    def insert_at(self, item, index):

        if index < 0 or index > self.length:
            print("please enter appropriate index")
            return
        
        if self.length == self.capacity:
            self.__resize(2*self.capacity)
        
        for i in range(self.length-1, index-1, -1):
            self.array[i+1] = self.array[i]
        
        self.array[index] = item
        self.length += 1
        if index == 9:
            print('tghjk')
        
        print(f"item {item} inserted to {index} index, array length is {self.length}")


    def removeat(self, index):

        if self.length == 1 and index == 0:

            self.array = None
            self.length = 0
            self.capacity = 2
            return

        elif self.capacity/4 >= self.length:
            self.__resize(int(self.capacity/2))
            print(f"from remove at capacity is {self.capacity}")

        elif index < 0 and index >= self.length: 
            print('index out of bound ')
            return

       
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        

        self.array[self.length-1] = None
        self.length -= 1
        print(f"array length is {self.length}")
        self.print_items()

    def __resize(self, new_cap):

        new_array = self.make_array(new_cap)

        if self.length == 0: 
            self.array = None
            return

        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array
        del new_array
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object)()
       
    def print_items(self):
        print(f"array capacity: {self.capacity}")

        if hasattr(self.array, '_objects'):
            array = [self.array._objects[i] for i in self.array._objects] 
            print(array)
        else:
            print("[]")
            





