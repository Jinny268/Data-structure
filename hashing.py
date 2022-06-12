# 선형조사
class Dictionary:
    def __init__(self, size):
        self.M = size
        self.keyList = [None]*size
        self.valueList = [None]*size

    def hashFunc(self, key):
        return key % self.M

    def put(self, key, value): # 삽입: linear probing
        initialPos = self.hashFunc(key)
        i =  initialPos
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            i = (i + 1) % self.M
            if i == initialPos:
                return

    def get(self, key): # 검색(탐색)
        initialPos = self.hashFunc(key)
        i =  initialPos
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            i = (i + 1) % self.M
            if i == initialPos:
                return 



# 제곱조사(이차조사)
class Dictionary:
    def __init__(self, size):
        self.M = size      # 테이블 크기
        self.keyList = [None]*size
        self.valueList = [None]*size
        self.N = 0         # 저장된 항목 수

    def hashFunc(self, key):
        return key % self.M

    def put(self, key, value): # 삽입: quadratic probing
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            j += 1
            i = (initialPos + j*j) % self.M
            if self.N > self.M:
                return

    def get(self, key):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            j += 1
            i = (initialPos + j*j) % self.M
        return None

# 이중해싱
class DoubleHashing:
    def __init__(self, size):
        self.M=size
        self.a=[None for x in range(size+1)]   # 해시테이블
        self.d=[None for x in range(size+1)]   # key관련 데이터 저장
        self.N=0   # 항목 수

    def hash(self, key):   # 나눗셈 함수
        return key%self.M

    def put(self, key, data):   # 삽입 연산
        initial_position=self.hash(key)   # 초기 위치
        i=initial_position
        d=7-(key%7)
        j=0
        while True:
            if self.a[i]==None:   # 삽입 위치 찾기
                self.a[i]=key   # key를 해시테이블에 저장
                self.d[i]=data   # key관련 데이터를 동일한 인덱스 안에 저장
                self.N+=1
                return
            if self.a[i]==key:   # 이미 key가 존재한다면
                self.d[i]=data   # 데이터만 교체
                return
            j+=1
            i=(initial_position+j*d)%self.M   # i의 다음 위치
            if self.N>self.M:   # 테이블이 full이면
                break
            
    def get(self, key):   # 탐색 연산
        initial_position=self.hash(key)
        i=initial_position
        d=7-(key%7)
        j=0
        while self.a[i]!=None:   # a[i]가 비어있지 않으면
            if self.a[i]==key:
                return self.d[i]   # 탐색 성공
            j+=1
            i=(initial_position+j*d)%self.M   # i의 다음 위치
        return None   # 탐색 실패
