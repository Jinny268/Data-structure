# 전위 순회 ( 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리 )
class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        self._subtreePreorder(self.root)

    def _subtreePreorder(self, p):
        if p is not None:
            print(p.data)
            self._subtreePreorder(p.left)
            self._subtreePreorder(p.right)

# 중위 순회 ( 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리 )
class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        self._subtreeInorder(self.root)

    def _subtreeInorder(self, p):
        if p is not None:
            self._subtreeInorder(p.left)
            print(p.data)
            self._subtreeInorder(p.right)

# 후위 순회 ( 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트 )
class BinaryTree:
    def __init__(self):
        self.root = None

    def postorder(self):
        self._subtreePostorder(self.root)

    def _subtreePostorder(self, p):
        if p is not None:
            self._subtreePostorder(p.left)
            self._subtreePostorder(p.right)
            print(p.data)

# 이진 트리 연산 - 높이, 노드 개수, 단말 노드의 수
class BinaryTree: 
    def __init__(self):
        self.root = None

    def height(self):
        return self._subtreeHeight(self.root)

    def _subtreeHeight(self, p):
        if p is None:
            return 0
        else:
            hleft = self._subtreeHeight(p.left)
            hright = self._subtreeHeight(p.right)
            return max(hleft, hright)+1

    def size(self):
        return self._sudtreeSize(self, root)
    
    def _sudtreeSize(self, p):
        if p is None:
            return 0
        else:
            return 1 + self._sudtreeSize(p.left) + self._sudtreeSize(p.right)

    def _sudtreeCountLeaf(self, p):
        if p if None:
            return 0
        elif p.left is None and p.right is None:
            retuen 1
        else:
            return self._sudtreeCountLeaf(p.left) + self._sudtreeCountLeaf(p.right)
