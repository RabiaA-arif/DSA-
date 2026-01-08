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

obj.printll()