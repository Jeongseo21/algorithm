# delete 설계

# 1. leafNode를 삭제할 경우
# leafNode : Child Node가 없는 Node
#  - 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

# 2. Child Node가 하나인 Node를 삭제할 경우
#   - 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

# 3. Child Node가 두 개인 Node를 삭제할 경우
#  - 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
#  - 혹은 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
# 여기까지는 알아두기

# 이 이상은 면접에서 물어보지 않음.
# 4. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent가 가리키게 할 경우
#  - 삭제할 Node의 오른쪽 자식을 선택한다.
#  - 오른 쪽 자식의 가장 왼쪽의 Node를 선택한다.
#  - 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 한다.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:  # 입력한 value가 head의 value보다 작으면
                if self.current_node.left != None:  # head node의 왼쪽자식이 있으면
                    self.current_node = self.current_node.left  # 왼쪽자식으로 head node가 이동
                else:
                    self.current_node.left = Node(value)
                    break
            else:  # 입력한 value가 head의 value보다 크거나 같으면
                if self.current_node.right != None:  # head node의 오른쪽 자식이 있으면
                    self.current_node = self.current_node.right  # 오른쪽 자식으로 head node가 이동
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value < value:
                self.current_node = self.current_node.right
            else:
                self.current_node = self.current_node.left
        return False


def delete(self, value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
        if self.current_node.value == value:  # 삭제할 node를 찾음
            searched = True
            break
        elif value < self.current_node.value:  # 현재 node를 parent_node로 바꾸고 left자식을 현재node로 변경
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:  # 현재 node를 parent_node로 바꾸고 right자식을 현재 node로 변경
            self.parent = self.current_node
            self.current_node = self.current_node.right
    if searched == False:
        return False

    # 이제 current_node는 삭제할 node를 가리키고 있고, parent_node는 그 부모 node를 가리키고 있음

    # 1번 케이스 : 삭제할 Node가 leafNode일 경우
    if self.current_node.left == None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left == None
        else:
            self.parent.right == None
        del self.current_node
    # 2번 케이스
    if self.current_node.left != None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    elif self.current_node.left == None and self.current_node.right != None:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right


head = Node(1)
BT = NodeMgmt(head)
BT.insert(2)
BT.insert(3)
BT.insert(4)
print(BT.search(2))
print(BT.search(5))

# 이진탐색트리의 시간복잡도와 단점

# 이진탐색트리의 시간복잡도
# depth(트리의 높이)를 h라고 하면, 시간복잡도는 O(h)이다.
# 입력된 데이터의 개수가 1->3->7->15 로 증가함에 따라 시간복잡도는 1->2->3->4로 증가하고 이는 log(n)과 가깝다
# 따라서 h = log(n) 이므로 시간복잡도는 O(log(n))이다.

# 또는 한번 판단할 때 마다 절반 씩 탐색할 데이터가 없어지기 때문에 O(log(n))이라고 볼 수 있다.

# 이진탐색트리의 단점
# 평균 시간복잡도 O(log(n))은 이진트리가 균형잡혀 있을 때의 평균 시간복잡도이다.
# 트리의 노드가 한 쪽으로만 치우쳐 있을 경우에는 최악의 경우 링크드리스트와 동일한 O(n)의 시간복잡도를 가질 수도 있다.
