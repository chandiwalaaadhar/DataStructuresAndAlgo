# Create a Node Class that has charateristics of a Node of LL
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data=data  # This is the variable where data is stored
        self.next=next  # This is the variable in which pointer to the next node is stored
        self.prev=prev
    
# Create a Singly LinkedList Class
class SinglyLinkedList(object):
    def __init__(self, node=None):
        self.length=0
        self.head=node
    
    def insertAtBeg(self, data):
        '''Insert the Node at Beginning'''
        newNode=Node()
        newNode.data=data
        if (self.length==0):
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1

    def insertAtEnd(self, data):
        '''Function to Traverse through the List and Insert node at end'''
        newNode=Node()
        newNode.data=data
        if (self.head is None):
            self.head=newNode
        
        else:
            current=self.head
            while (current.next!=None):
                current=current.next
            current.next=newNode
        self.length+=1

    def insertAtPos(self, data, pos):
        '''Function to Traverse through the List and Insert the node at a particular posititon
        Note: The position starts from 0'''
        newNode=Node()
        newNode.data=data
        if(self.length==0):
            self.head=newNode
        if(pos==0):
            newNode.next=self.head
            self.head=newNode
        else:
            count=1
            current=self.head.next
            prev=self.head
            while (count!=pos):
                count+=1
                current=current.next
                prev=prev.next
            prev.next=newNode
            newNode.next=current
        self.length+=1

    def delAtBeg(self):
        if (self.head!=None):
            current=self.head
            self.head=current.next
            self.length-=1
        else:
            print('Empty List')

    def delFromEnd(self):
        if (self.head.next==None):
            self.head=None

        if(self.head!=None):
            current=self.head
            while(current.next.next!=None):
                current=current.next
            current.next=None
            self.length-=1


    def printList(self):
        '''Function to Traverse through the List and Print all Elements'''
        temp=self.head
        while (temp.next!=None):
            print(temp.data)
            temp=temp.next
        print(temp.data)

    def len_list(self):
        '''Function to Print Length of list'''

        print("The Length of the Linked List is %d" %self.length)

class DoublyLinkedLists(object):
    def __init__(self, node=None):
        self.length=0
        self.head=node
    
    def insertAtBeg(self, data):
        newNode=Node()
        newNode.data=data
        if(self.length==0):
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        self.length+=1
    
    def insertAtEnd(self, data):
        newNode=Node()
        newNode.data=data
        current=self.head
        if(self.length==0):
            self.head=newNode
        else:
            while(current.next!=None):
                current=current.next
            current.next=newNode
            newNode.prev=current
        self.length+=1

    def insertAtPos(self, data, pos):
        newNode=Node()
        newNode.data=data
        if(self.length==0):
            self.head=newNode
            self.length+=1
            return
        if(pos==0):
            self.insertAtBeg(data)
            self.length+=1
            return
        if(pos==self.length):
            self.insertAtEnd(data)
            self.length+=1
            return
        else:
            count=1
            current=self.head.next
            previous=self.head
            while (count!=pos):
                count+=1
                current=current.next
                previous=previous.next
            previous.next=newNode
            newNode.prev=previous
            newNode.next=current
            current.prev=newNode
            self.length+=1
            return

    def delFromEnd(self):

        if(self.length==0):
            raise ValueError()

        if(self.length==1):
            self.head=None
            self.length-=1
            return
        
        else:
            current=self.head.next
            previous=self.head
            while(current.next!=None):
                current=current.next
                previous=previous.next
            previous.next=None
            current.prev=None
            self.length-=1
            return

    def delFromBeg(self):

        if(self.length==0):
            raise ValueError

        else:
            self.head=None
            self.length-=1
            return

    def delFromPos(self, pos):

        if(self.length==0):
            return

        if(pos>self.length):
            raise LookupError

        if(pos==self.length):
            self.delFromEnd()

        else:
            count=1
            current=self.head.next
            previous=self.head
            while (count!=pos):
                count+=1
                current=current.next
                previous=previous.next
            previous.next=current.next
            current.prev=None
            current.next.prev=previous
            current.next=None
            self.length-=1
            return



    def printList(self):
        '''Function to Traverse through the List and Print all Elements'''
        current=self.head
        if(self.length==0):
            print("Empty list")
            return
        while (current.next!=None):
            print(current.data)
            current=current.next
        print(current.data)
        

if __name__ == "__main__":
    linkedlist1=DoublyLinkedLists()
    #linkedlist1.insertAtBeg(10)
    #linkedlist1.insertAtBeg(20)
    #linkedlist1.insertAtEnd(30)
    #linkedlist1.insertAtPos(40, 1)
    linkedlist1.insertAtEnd(80)
    linkedlist1.delFromPos(4)
    linkedlist1.printList()