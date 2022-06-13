class MaxHeap:   # 최대 힙의 구현
    def __init__(self):
        self.heap = []

    def print(self):
        print(self.heap)

    def insert(self, value):   # 원소 삽입
        self.heap.append(value)
        i = len(self.heap) - 1
        while (i != 0 and value > self.heap[(i-1)//2]):
            self.heap[i] = self.heap[(i-1)//2]
            i = (i-1)//2
        self.heap[i] = value

    def delete(self):   # 최대 원소 삭제
        n = len(self.heap)
        if n == 0:
            return None
        current = 0
        maxValue = self.heap[0] # 최대값 저장
        value = self.heap[n-1]  # 마지막 원소를 value에 저장
        self.heap.pop()  # 마지막 원소 삭제
        n = n – 1        # 원소 하나가 삭제되어 n을 1 줄임
        while (2*current+1 < n):   # current가 leaf가 아니면
            leftChild = 2*current + 1
            rightChild = leftChild + 1
            # 두 자식 노드 중 큰 값의 노드를 largerChild
            if rightChild < n and self.heap[rightChild] > self.heap[leftChild]:
                largerChild = rightChild
            else:
                largerChild = leftChild
                
            if value < self.heap[largerChild]: # largerChild의 값이 크면
                self.heap[current] = self.heap[largerChild]
                current = largerChild          # current를 largerChild로 내림
            else:
                break
        self.heap[current] = value
        return maxValue

# 힙을 저장하는 효과적인 자료구조는 배열이다.
# 우선순위 큐의 가장 좋은 구현 방법은 힙이다.
# 힙이란 완전이진트리 기반의 자료구조이다. 가장 큰(또는 가장 작은) 값을 빠르게 찾아내도록 만들어진 자료구조이다.
# 최대 힙은 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전이진트리이다.
# 최소 힙은 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진트리이다.
# n개의 노드를 가지는 완전이진트리 높이: [log2n]+1
# 최대 힙의 연산에는 원소 삽입(최대 키의 원소 찾기), 최대 키의 원소 삭제가 있다.
# 힙의 삽입 연산(upheap)은 먼저 힙의 마지막 노드의 바로 다음에 비어있는 원소에 새로운 항목을 저장하고, 다음으로 루트 방향으로 올라가면서 부모의 키와 비교하여 힙 속성이 만족될 때까지 노드를 교환하면 된다.
# 힙의 최소키 원소 삭제 연산(downheap)은 먼저 가장 마지막 노드의 항목을 루트로 옮기고, 힙 크기를 1씩 감소시킨다. 그 다음 루트로부터 자식들 중에서 작은 값을 가진 자식과 키를 비교하여 힙속성이 만족될 때까지 키를 교환하며 이파리 방향으로 진행한다.
# 힙은 보통 배열을 이용하여 구현한다. ( 완전이진트리 -> 각 노드에 번호를 붙임 -> 배열의 인덱스 )
# 파이썬은 우선순위큐를 위한 heapq를 라이브러리로 제공한다. Import heapq으로 선언한다. insert() 메소드와 동일한 heapq.heappush(heap, item), delete_min() 메소드와 동일한 heapq.heappop(heap), item 삽입 후 delete_min() 수행하는 heapq.heappushpop(heap, item), 리스트 h를 힙으로 만드는 heapq.heapify(h)가 있다.
