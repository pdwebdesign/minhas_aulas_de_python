class No(object):
    def __init__(self,key,value=None,left=None,right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def get(self,key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self
    def __str__(self):
        return str(self.key)
    def add(self,node):
         if node.key < self.key:
             if self.left is None:
                 self.left = node
             else:
                 self.left.add(node)
         else:
             if self.right is None:
                 self.right = node
             else:
                 self.right.add(node)
    def traverse(self, visit, order="pre"):
        if order == 'pre':
            visit(self)
        if self.left is not None:
            self.left.traverse(visit,order)
        if order == 'in':
            visit(self)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'post':
            visit(self)

root = No(42)
root.left = No(10)
root.right = No(90)
root.left.left = No(2)
found = root.get(20)
if found:
    print(found.key)

novo = No(30)
root.add(novo)
root.traverse(print,'post')

