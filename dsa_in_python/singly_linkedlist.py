class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
        
        
class singly_linkedlist:
    def __init__(self,head=None):
        self.head=head
    
    
    def insert_node_at_end(self,value):
        temp=Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
            
        else:
            self.head=temp
    
    def insert_node_at_begning(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
    
    
    
    def insert_node_at_mid(self,value,x):
        temp=Node(value)
        t1=self.head
        
        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next
        
    def deletell(self,value):
        temp1=self.head
        prev=temp1
        while(temp1.next!=None):
            if(temp1.data==value):
                prev.next=temp1.next
                break
            else:
                prev=temp1
                temp1=temp1.next
    
    def printll(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)   
            
            
obj=singly_linkedlist()
obj.insert_node_at_end(1)
obj.insert_node_at_end(2)
obj.insert_node_at_end(3)
obj.insert_node_at_end(4)

obj.printll()

obj.insert_node_at_begning(10)
obj.insert_node_at_begning(20)
obj.insert_node_at_begning(30)
obj.insert_node_at_begning(40)
obj.insert_node_at_begning(50)

obj.insert_node_at_mid(35,20)
obj.insert_node_at_mid(11,10)
obj.deletell(30)
obj.printll()