class Stack:
    '''Implementing Stack with reducable capacity as required'''
    def __init__(self, capacity=1):
        self.top=-1
        self.capacity=capacity
        self.A=[None]*capacity
    def push(self,data):
        if(self.top+1==self.capacity):
            print("Trying to resize")
            self.resize()
        if(self.isFull()):
            print('stack overflow')
            return
        self.top+=1
        self.A[self.top]=data
    def resize(self):
        self.capacity=self.capacity*2
        newArr=[None]*self.capacity
        for i in range(self.top+1):
            newArr[i]=self.A[i]
        self.A = newArr
    def pop(self):
        if(self.top==-1):
            print("stack underflow")
            return
        temp=self.A[self.top]
        self.top-=1
        if(self.top<self.capacity//2):
            print('reducing the capacity')
            self.capacity=self.capacity//2
            newArr=[None]*self.capacity
            for i in range(self.top+1):
                newArr[i]=self.A[i]
            self.A=newArr
        return temp
    def peek(self):
        if(self.top==-1):
            print("stack underflow")
            return
        return self.A[self.top]
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top+1 == self.capacity
