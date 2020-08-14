# 일반적으로 햅 구현시 배열 자료구조를 활용함
# root노드의 인덱스 번호를 1로 지정하면 구현이 좀 더 수월함
# 부모노드 인덱스 번호 = 자식노드 인덱스 번호 // 2
# 왼쪽 자식노드의 인덱스 번호 = 부모노드 * 2
# 오른쪽 자식노드의 인덱스 번호 = 부모노드 * 2 + 1
# 배열로 힙을 나타내면 부모노드, 자식노드의 인덱스번호를 간편하게 알아낼 수 있어서 유용

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    
    # 자식이 부모보다 값이 크면 True반환
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else: 
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        #move_up이 True인 경우 부모노드와 swap
        inserted_idx = len(self.heap_array)-1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True
    

    def move_down(self, poped_idx):
        left_child_poped_idx = poped_idx * 2
        right_child_poped_idx = poped_idx * 2 + 1

        # case1: 자식노드가 하나도 없을 때
        if left_child_poped_idx >= len(self.heap_array):
            return False
        # case2: 왼쪽 자식노드는 있으나 오른쪽은 없을 때
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                return True
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 둘 다 있을 때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False


    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            left_child_poped_idx = poped_idx * 2
            right_child_poped_idx = poped_idx * 2 + 1

            # case2: 왼쪽 자식노드는 있으나 오른쪽은 없을 때
            if right_child_poped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_poped_idx
                
            # case3: 왼쪽, 오른쪽 자식 둘 다 있을 때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_poped_idx
                    
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_poped_idx
        
        return returned_data
                    
            
heap = Heap(5)
heap.insert(4)
heap.insert(10)
heap.insert(8)
heap.insert(15)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)



### 시간복잡도 ###
# 완전이진트리이기 때문에 자료의 개수와 depth의 관계가 log(n)이다. 따라서 시간복잡도도 O(log(n)) 
# 체크할 횟수가 50프로씩 감소하기 때문에 O(log(n))이다.