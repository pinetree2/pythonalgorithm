#이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any,Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self,key:Any,value:Any, left : Node = None, right : Node = None):
        """생성자"""
        self.key= key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:

    """이진 검색 트리"""
    def __init(self):
        """초기화"""
        self.root = None #루트

    def search(self,key:Any) -> Any:
        """키가 key인 노드를 검색"""
        p = self.root #루트에 주목
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value #검색성공
            elif key < p.key:# key쪽이 작으면
                p = p.left
            else:
                p = p.right

    def add(self,key:Any,value:Any) -> bool:
        """키가 key이고, 값이 value인 노드 삽입"""
        def add_node(node : Node, key:Any,value:Any) -> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입"""
            if key ==node.key:
                return False #key가 이진트리에 이미 존재
            elif key<node.key:
                if node.left is None:
                    node.left = Node (key,value,None,None)
                else:
                    add_node(node.left, key.value)
            else:
                if node.right is None:
                    node.right = Node(key,value,None,None)
                else:
                    add_node(node.right,key,value)
            return True

        #트리가 빈 상태
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        #트리가 비어있지 않을때 재귀호출함.
        else:
            return add_node(self.root,key,value)

    def remove(self,key:Any)->bool:
        """키가 key인 노드를 삭제"""
        # 스캔중인노드
        p = self.root
        # 스캔 중인 노드의 부모 노드
        parent = None
        is_left_child = True # p는 parent의 왼쪽 자식 노드인지 확인

        #삭제할 키 검색
        while True:
            if p is None: #더이상 진행할 수 없으면
                return False #그 키는 존재하지 않음

            if key == p.key:
                break #key와 노드 p의 키가 같으면 검색성공

            else:
                parent = p #부모설정
                if key < p.key: #key가 작으면
                    is_left_child = True #왼쪽자식
                    p = p.left #왼쪽서브트리에서 검색

                else:
                    is_left_child = False
                    p = p.right

        # 만약 삭제하는 노드가 자식노드가 없을때,자식노드가 한개인 노드를 삭제할때
        if p.left is None: #p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right #부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right #부모의 오른쪽 포인터가 오른쪽 자식을 가리킴

        elif p.right is None: #p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left #부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left #부모의 오른쪽 포인터가 왼쪽 자식을 가리킴


        #자식노드가 2개인경우우
        else:
            parent = p
            left = p.left # 서브트리안에서 가장 큰 노드 (왜..?)
            is_left_child = True
            while left.right is not None: #가장 큰 노드 left검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key #left의 키를 p로 이동
            p.value= left.value #left의 데이터를 p로 이동

            #left삭제
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True


        def dump(self) -> None:
            """===모든 키의 노드를 오름차순으로 출력"""
            def print_subtree(node: Node):
                """node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력"""
                if node is not None:
                    print_subtree(node.left)
                    print(f'{node.key} {node.value}')
                    print_subtree(node.right)

            print_subtree(self.root) #재귀함수


            #최소키와 최대키를 반환하는 함수
        def min_key(self) -> Any:
            if self.root is None:
                return None
            p = self.root
            while p.left is not None:
                p = p.left
                return p.key

            def max_key(self) -> Any:
                if self.root is None:
                    return None
                p = self.root
                while p.right is not None:
                    p = p.right
                return p.key









