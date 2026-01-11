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