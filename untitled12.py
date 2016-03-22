class Tree:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        
    def __iter__(self):
        if not self.right  and not self.left:
            yield self.value
        if self.right:
            for i in self.left:
                yield i
        if self.left:
            for k in self.right:
                yield k
            
        
        
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        repr(self.right)
        print(self.value)
        repr(self.left)
        
    
tree = Tree(0, Tree(1, Tree(3), Tree(4)),                             
               Tree(2))

print(list(tree) )

    
       
        
        






