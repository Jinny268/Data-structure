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

# 트리란 계층적인 자료의 표현에 적합한 자료 구조이다.
# 노드의 차수는 자식 노드의 수이다.
# 트리의 차수는 노드의 최대 차수이다.
# 단말 노드는 자식 노드가 없는 노드이며, 비단말 노드는 자식 노드가 있는 노드이다.
# 루트 노드는 가장 위에 있는 노드로 차수가 가장 크다.
# 차수는 가장 아래에 있는 레벨부터 루트 노드까지 0, 1, 2, 3, ... 순으로 세면 된다.
# 레벨은 루트 노드부터 가장 아래에 있는 노드까지 1, 2, 3, ... 순으로 세면 된다.
# Ordered Tree는 각 노드의 자식 노드들의 순서가 의미가 있는 트리이다.
# 이진트리는 재귀적으로 정의되며, 어떤 노드의 자식의 수가 최대 2개를 넘지 않는 트리를 말한다.
# 포화 이진트리란 트리의 각 레벨에 노드가 꽉 차있는 이진트리이다.
# 완전 이진트리란 높이가 h일 때 레벨 1부터 h-1까지는 노드가 모두 채워지며, 마지막 레벨 h에서는 왼쪽부터 노드가 순서대로 채워진다.
# 이진트리는 노드의 개수가 n개이면 간선의 개수는 n-1개이다.
# 레벨 k에 있는 최대 노드의 수는 2^(k-1)이다.
# 높이가 h이면 h~(2^h-1)개의 노드를 가진다.
# n개의 노드의 이진 트리의 높이는 {log2(n+1)}~n개이다. ([log2(n+1)]=[log2n]+1)
# 이진트리의 배열표현법(1)은 각 노드에 1번부터(0부터 할 수 도 있음) 번호를 붙이고 (레벨이 낮은 노드들부터 높은 노드들 순서대로, 같은 레벨은 왼쪽부터 오른쪽으로 차례대로 번호를 붙임), 그 번호를 배열의 인덱스로 하여 노드의 데이터를 배열에 저장하는 방법
# 편향 이진트리의 경우 배열표현법(1)을 이용하면 메모리 낭비가 심하다.
# 배열표현법(2)는 2차원리스트를 이용한다.
# 이진트리의 연결구조 표현법은 부모노드가 자식노드를 참조하도록 한다. 링크가 두개만 있으면 표현이 가능하다.
