'''
ALGORITHM:
1. Define a Node class which represents a node in the list. It will have three properties: data, previous which will point to the previous node and next which will point to the next node.
2. Define another class for creating a doubly linked list, and it has two nodes: head and tail. Initially, head and tail will point to null.
3. addNode() will add node to the list:
  - It first checks whether the head is null, then it will insert the node as the head.
  - Both head and tail will point to a newly added node.
  - Head's previous pointer will point to null and tail's next pointer will point to null.
  - If the head is not null, the new node will be inserted at the end of the list such that new node's previous pointer will point to tail.
  - The new node will become the new tail. Tail's next pointer will point to null.
4. a display() will show all the nodes present in the list.
  - Define a new node 'current' that will point to the head.
  - Print current.data till current points to null.
  - Current will point to the next node in the list in each iteration.

'''

#Represent a node of doubly linked list    
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class DoublyLinkedList:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
            #Both head and tail will point to newNode    
            self.head = self.tail = newNode;    
            #head's previous will point to None    
            self.head.previous = None;    
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None;    
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
            #newNode's previous will point to tail    
            newNode.previous = self.tail;    
            #newNode will become new tail    
            self.tail = newNode;    
            #As it is last node, tail's next will point to None    
            self.tail.next = None;    
                
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.data),;    
            current = current.next;    
                
dList = DoublyLinkedList();    
#Add nodes to the list    
dList.addNode(1);    
dList.addNode(2);    
dList.addNode(3);    
dList.addNode(4);    
dList.addNode(5);    
     
#Displays the nodes present in the list    
dList.display();  
