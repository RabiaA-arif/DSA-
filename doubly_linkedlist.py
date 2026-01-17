class Node:
    def __init__(self,value=None):
        self.data=value
        self.prev=None
        self.next=None
        
        
        
class DoublyLL:
    def __init__(self):
        self.head=None
        
        
    def insert_at_end(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return 
        
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
                
            t.next=temp
            temp.prev=t
    def insert_at_begning(self,value):
        temp=Node(value)    
        if(self.head==None):
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
        
            
    def printDLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data,end=" <-->" )
            t1=t1.next
        print(t1.data)
        
obj=DoublyLL()
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.insert_at_begning(5)
obj.printDLL()