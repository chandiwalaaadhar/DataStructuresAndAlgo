# Create a Node Class that has charateristics of a Node of LL
class Node:
    def __init__(self, data=None, next=None):
        self.data=data  # This is the variable where data is stored
        self.next=next  # This is the variable in which pointer to the next node is stored
    
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
        if(self.head is None):
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
