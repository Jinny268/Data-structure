# 반복 이용
def binarySearch(a, key):   # 반복 
    left = 0  # a = [ .....]
    right = len(a)-1

    while left <= right:
        mid = (left + right)//2
#       print(a[mid])
        if key == a[mid]:
            return True   # return mid
        elif key < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False   # return -1

# 재귀 이용
def binarySearch1(a, key, left, right): 
    if left > right:
        return False
    else:
        mid = (left + right)//2
#       print(a[mid])
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binarySearch1(a, key, left, mid-1)
        else:
            return binarySearch1(a, key, mid+1, right)

# 이진탐색트리
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key         # 키 (key)
        self.value = value    # 값 (value)
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        
    # 탐색 연산 - 수행시간 O(h)
    def search1(self, key):   # 반복 구조
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def search2(self, key):   # 재귀 이용
        return self._searchBst(self.root, key)

    def _searchSubtree(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._searchSubtree(node.left, key)
        else:
            return self._searchSubtree(node.right, key)

    def _minNode(self):   # 최소 키를 찾는 연산
        node = self.root
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node.key

    def _maxNode(self):   # 최대 키를 찾는 연산
        node = self.root
        if node is None:
            return None
        while node.right != None:
            node = node.right
        return node.key

    # 삽입 연산 알고리즘
    def insert(self, key, value):
        self.root = self._insertSubtree(self.root, key, value)

    def _insertSubtree(self, node, key, value): 
        if node == None:               
            return TreeNode(key, value)
        elif key < node.key:              # 왼쪽 부트리에 노드를 삽입 
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:              # 오른쪽 부트리에 노드를 삽입
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass
        return node

    # 삭제 연산
    def delete(self, key):
        self.root = self._deleteSubtree(self.root, key)
        
    def _deleteSubtree(self,node,key):
        if node == None:
            return None
       if key < node.key:   # 삭제할 키의 노드가 node의 왼쪽 부트리인 경우
            node.left = self._deleteSubtree(node.left, key)
            return node
        elif key > node.key:   # 삭제할 키의 노드가 node의 오른쪽 부트리인 경우
            node.right = self._deleteSubtree(node.right, key)
            return node
        else:   # node가 삭제할 키의 노드인 경우
            if node.right == None:   # node의 오른쪽 자식노드가 없을 경우
                return node.left
            if node.left == None:   # node의 왼쪽 자식노드가 없을 경우
                return node.right
            
            rightMinNode = self._minNode(node.right)   # node의 오른쪽 부트리에서 최소키의 노드를 찾음
            node.key = rightMinNode.key   # node의 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
            node.value = rightMinNode.value
            node.right = self._deleteSubtree(node.right, rightMinNode.key)   # node의 오른쪽 부트리에서 최소키의 노드를 삭제        
            return node

    
