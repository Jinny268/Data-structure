class Node:
    def __init__(self,element):
        self.data = element
        self.link = None

# 연결리스트를 만드는 방법 1: insertFront를 이용
def insertFront(head, e):   #
    node = Node(e)
    node.link = head
    return node

head = None
head = insertFront(head, 30)
# head -> 30
head = insertFront(head, 20)
# head -> 20 -> 30
head = insertFront(head, 10)
# head -> 10 -> 20 -> 30
head = insertFront(head, 50)
# head -> 50 -> 10 -> 20 -> 30

node = head
while node != None:
    print(node.data, end = ' ')
    node = node.link
    
print()

def printList(head):
    node = head
    while node != None:
        print(node.data, end = ' ')
        node = node.link
    print()

# 클래스를 이용한 연결리스트     
class LinkedList:
    def __init__(self):
        self.head = None
  
    def insertFront(self, e):
        node = Node(e)
        node.link = self.head
        self.head =  node

    def getNode(self, pos):
        if pos < 0:
            return None
        node=self.head
        while pos>0 and node!=None:
            node = node.link
            pos-=1
        return node

    def getEntry(self, pos):
        node=self.getNode(pos)
        if node==None:
            return None
        else:
            return node.data

    def size(self):   # iterative version (반복을 이용)
        count = 0
        current  = self.head
        while current is not None:
            count += 1
            current = current.link 
        return count

    '''
    # recursive version
    def nodeCount(self, node):
        if node == None:
            return 0
        else:
            return self.nodeCount(node.link)+1

    def size(self):
        return self.nodeCount(self.head)

    '''

    def insert(self, pos, e):
        if pos < 0 or pos > self.size():
            print("위치 error")
            return
        node = Node(e)
        before =self.getNode(pos-1) # before 노드 찾음 
        if before == None:   # 맨 앞에 삽입
            node.link = self.head
            self.head = node
        else:   # 중간에 삽입
            node.link = before.link
            before.link = node

    def delete(self, pos):
        if pos < 0 or pos >= self.size():
            print("위치 error")
            return None
        before = self.getNode(pos-1)
        if before == None:                   # 시작 노드 삭제
            e = self.head.data
            self.head = self.head.link
        else:                                      # 중간에 있는 노드 삭제
            e = before.link.data
            before.link = before.link.link
        return e

    def find(self, item):
        pos = 0
        node  = self.head
        while node is not None: 
            if node.data == item:
                return pos
            else:   # 리스트에서 item이 없는 경우 -1을 반환
                pos += 1
                node = node.link 
                return -1

    def printList(self):
        node = self.head
        while node != None:
            print(node.data, end = ' ')
            node = node.link
        print()
            
def linkedListPractice():
    L = LinkedList()
    L.insertFront(20)
    L.insertFront(40)
    L.insertFront(30)
    L.printList()
    L.insertFront(25)
    L.printList()
    

linkedListPractice()
