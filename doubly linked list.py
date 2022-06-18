class DNode:   # 이중연결리스트 노드
    def __init__(self, e):
        self.addr = e
        self.next = None
        self.back = None

class DLinkekList:   # 이중연결리스트
    def __init__(self):
        head = None

'''
<새로운 노드 삽입>
newNode.back = location.back
newNode.next = location
if (location.back == None):   #  처음에 노드 삽입
    head = newNode
else: 
    location.back.next  = newNode
location.back = newNode

<노드 삭제>
if (location.back == None):   # 첫번째 노드 삭제
    head = location.next;
    if (location.next != None):   # 첫번째 노드가 마지막 노드가 아닌 경우
        location.next.back = None
else:   # 첫번째 노드 삭제가 아닌 경우
    location.back.next = location.next
    if (location.next != None):   # 마지막 노드 삭제가 아닌 경우 (중간 노드 삭제)
        location.next.back = location.back
'''

# 특정한 노드 이전에 새로운 노드를 삽입하는 것이 간편하다.
# 특정한 노드를 삭제하는 것이 간편하다.
# 현재 노드에서 이전 노드로 이동하는 것이 간편하다.
# 메모리 공간이 Singly linked list의 두 배가 필요한 것이 단점이다.
