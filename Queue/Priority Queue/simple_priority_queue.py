from collections import deque


class PriorityQueue(object):

    def __init__(self):

        self.queue = deque()
    
    def __str__(self):
        return ', '.join( [str(i) for i in self.queue])
    
    def isempty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)
    
    def poll(self):

        try:
            max = 0

            for i in range(len(self.queue)):

                if self.queue[i] > self.queue[max]:
                    max = i
            
            deqitem = self.queue[max]
            del self.queue[max]
            return deqitem
        except IndexError:
            print()
            exit()


priq = PriorityQueue()

priq.insert(12)
priq.insert(2)
priq.insert(4)
priq.insert(17)
priq.insert(3)
priq.insert(7)

print(f"priority queue items: {priq}")

while not priq.isempty():
    print(f"dequeued: {priq.poll()}")
