class CircularArray:
    def __init__(self, limit=5):
        self.queue=[]
        self.front=None
        self.rear=None
        self.limit=limit
        self.size=0

    def isEmpty(self):
        return self.size<=0

    def isFull(self):
        return (self.size==self.limit)

    def enQueue(self, item):
        if self.isFull():
            print("Queue is Full")
            return
        else:
            self.queue.append(item)
            if self.front is None:
                self.front=self.rear=0
            else:
                self.rear=self.size
            self.size+=1
            print("queue after enqueue" ,self.queue)
            
    
    def deQueue(self):
        if self.isEmpty():
            print("queue is already empty")
            return
        else:
            self.queue.pop(0)
            self.size-=1
            if(self.size==0):
                self.front=self.rear=None
            else:
                self.rear-=1
                print("queue after dequeue" ,self.queue)
                
    def size(self):
        return self.size



        
            