class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
    def display(self):
        print(self.element)

class LinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
        self.lst = []
         
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return
        first = self.head
        print(first.element)
        first = first.next
        while first:
            print(first.element)
            first = first.next
    
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e) 
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1


    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else:
            print("Removing")
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1

    def find_second_last_element(self):
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first
        else:
            print("Size not sufficient")
        return None

    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
        
    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False

    def rev_lst(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
        print("Reversed Linked List")
        LinkedList.display(self)
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size 
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size

            
L = LinkedList()
L.add_head(0)
L2 = LinkedList()
L2.add_head(2)
L2.add_head(5)
L2.add_head(8)
L2.add_head(13)
L2.add_tail(33)
print("Second Linked List")
L2.display()

print("Insertion at head (Ih) or tail (It)  Deletion at head (Dh) or tail (Dt) Searching (S) Reverse & Display (R)&(D) ConcatList (C) Display list (D) Break from loop (B)")

while True:
    ins = input("Enter a Choice (Ih)(It)(Dh)(Dt)(S)(R)(C)(D)(B): ")
    if ins=="Ih" or ins=="ih":
        while True:
            ah = input("enter value to insert at head: ")
            if ah=="B" or ah=="b":
                break
            L.add_head(ah)
            L.display()
            
    elif ins=="It" or ins=="it":
        while True:
            ah = input("enter value to insert at tail: ")
            if ah=="B" or ah=="b":
                break
            L.add_tail(ah)
            L.display()

    elif ins=="Dh" or ins=="dh":
        L.remove_head()
            
    elif ins=="Dt" or ins=="dt":
        L.remove_tail()
            
    elif ins=="S" or ins=="s":
     	ah = input("enter value to Serach: ")
     	L.search(ah)
     	 	
    elif ins=="R" or ins=="r":
        L.rev_lst()
     	
    elif ins=="C" or ins=="c":
        print("Merged List")
        L.merge(L2)
        L.display()
     	
    elif ins=="B" or ins=="b":
     	break

    elif ins=="D" or ins=="d":
        L.display()
     	
    else:
     	continue
