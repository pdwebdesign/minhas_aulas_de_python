class No(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.key)
    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self
    def add(self, node):
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
    def add2(self, key):
        """Adiciona elemento à subárvore
        """
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, No(key))
        else:
            node.add(key)
    def traverse(self, visit, order='pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in)
           visitando os nós com a função visit() recebida como parâmetro.
        """
        if order == 'pre':
            visit(self)
        if self.left is not None:
            self.left.traverse(visit, order)
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

novo = No(30)

#root.add(novo)

root.traverse(print, 'in')