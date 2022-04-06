from io import StringIO
import math
import sys


class MinHeap:

    def __init__(self, degree, maxsize):
        self.__maxsize = maxsize
        self.__heap = [None]*maxsize
        self.__heap[0] = sys.maxsize
        self.__sz = 0
        self.parent = [None]*maxsize
        self.child = [None]*maxsize
        self.degree = self.__max(2, degree)

        for i in range(self.__maxsize):
            self.parent[i] = int((i-1)/self.degree)
            self.child[i] = i*self.degree + 1


    def print(self):
        for i in range( (self.__sz//2)):
            print(f"Parent {str(self.__heap[i])} left child {str(self.__heap[2*i+1])} right child {str(self.__heap[2*i+2])}")
    
    def add(self, elem):
        self.__heap[self.__sz] = elem
        self.__swim(self.__sz)
        self.__sz += 1
    

    def poll(self):

        if self.isempty(): return None
        root = self.__heap[0] 
        self.__sz -= 1 
        self.__heap[0] = self.__heap[self.__sz]
        self.__heap[self.__sz] = None
        self.__sink(0)
        return root
    
    def peek(self):
        if self.isempty(): return None
        return self.__heap[0]
    
    def removeat(self, i):
        if self.isempty(): return None
        indexoflastelem = self.size() - 1
        removed_data = self.__heap[i]
        self.__swap(i, indexoflastelem)
        self.__heap[indexoflastelem] = None

        # check if the last element was removed
        if i == indexoflastelem: return removed_data
        
        elem = self.__heap[i]
        self.__sink(i)

        # i sinking did not work try swimming
        if self.__heap[i] == elem: self.__swim(i)
        return removed_data


    def clear(self):
        self.__sz = 0
        self.__heap.clear()
        print("heap cleared")

    def isempty(self):
        return self.__sz == 0
    
    def size(self):
        return self.__sz
    
    def __swap(self, cindex, pindex):
        self.__heap[cindex], self.__heap[pindex] = self.__heap[pindex], self.__heap[cindex]
    
    
    def __is_less(self, i, j):

        if self.__heap[i] < self.__heap[j]:
            return True
        
        return False
    
    def __swim(self, cindex):

        while self.__is_less(cindex, self.parent[cindex]):

            self.__swap(cindex, self.parent[cindex])
            cindex = self.parent[cindex]
    

    def __sink(self, pindex):
        
        while True:
            cindex = self.__minchild(pindex)
            if cindex == -1: break
            self.__swap(cindex, pindex)
            pindex = cindex
            cindex = self.__minchild(pindex)

    def __minchild(self, pindex):
        index = -1
        from_ = self.child[pindex]
        to = self.__min(self.__sz, from_ + self.degree)
        mincindex = pindex
        for cindex in range(from_, to):
            if self.__is_less(cindex, mincindex): 
                index = mincindex = cindex
        return index

    def print_heap(self, total_width=60, fill=' '):
        last_row = -1
        output = StringIO()

        for i, n in enumerate(self.__heap):
            row = int(math.floor(math.log(i+1, 2))) if i else 0

            if row != last_row:
                output.write('\n')
            
            
            column = 2**row
            col_width = int(math.floor((total_width*1) / column))
            if n is None:
                continue
            output.write(str(n).center(col_width, fill))
            last_row = row
        
        print(output.getvalue())
        print('-'*total_width)


    def __min(self, x, y):
        if x <= y:
            return x
        return y
    
    def __max(self, x, y):
        if x <= y:
            return y
        return x



minheap = MinHeap(2, 20)
minheap.add(10)
minheap.add(20)
minheap.add(5)
minheap.print()
print("10, 20, 5 eklendi")
minheap.add(17)
minheap.add(4)
minheap.add(13)
minheap.print()
print("17, 4, 13 eklendi")
minheap.add(25)
minheap.add(6)
minheap.add(3)
minheap.print()
print("25, 6, 3 eklendi")
minheap.add(16)
minheap.add(12)
minheap.add(11)
minheap.print()
print("16, 12, 11 eklendi")
polled = minheap.poll()
print(f"polled {polled}")
minheap.print()
print(f"peek {minheap.peek()}")
minheap.add(0)
minheap.removeat(7)
minheap.print()
minheap.print_heap()



