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

root = No(42)
root.left = No(10)
root.right = No(90)
root.left.left = No(2)
found = root.get(20)
if found:
    print(found.key)


