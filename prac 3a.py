class Deque:
    def __init__(self):
    	self.items = []
    def isEmpty(self):
    	return self.items ==[]
    def addFront(self,items):
    	self.items.append(items)
    def addLast(self,items):
    	self.items.insert(0,items)
    def removeFront(self):
    	return self.items.pop()
    def removeLast(self):
    	return self.items.pop(0)
    def size(self):
    	return len(self.items)
    def display(self):
    	print(self.items)
D = Deque()
D.addFront(1)
D.addFront(11)
D.addFront(21)
D.addLast(4)
D.addLast(14)
D.addLast(24)
print("adding from head and tail")
D.display()
D.removeFront()
D.removeLast()
print("removing from head and tail")
D.display()
