import linked_list as link

class Stack:
    def __init__(self):
        self.stacked = link.LinkedList()

    def push(self, data):
        self.stacked.set_head(data)

    def pop(self):
        self.stacked.pop(0)

    def top(self):
        return self.stacked.head.data
    
    def size(self):
        return self.stacked.len
    
    def is_empty(self):
        return True if self.stacked.head == None else False
    
    def __str__(self):
        return str(self.top())
    
    def __len__(self):
        return self.size()