from msilib.schema import Class


class Node ():
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last =None

    def enque(self,val):
        node = Node(val)
        if (self.first==None):
            self.first=self.last=node
        else:
            self.last.next =node
            self.last = node
    def dequeue (self):
        if (self.first != self.last):
            self.first = self.first.next
        else:
            self.first = self.last = None

a =b = 0
print(a,b)