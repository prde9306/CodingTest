#이진 트리 검색
def search(self, key: Any) -> Any:
    p = self.root
    while True:
        if p is None:
            return None
        if key ==p.key:
            return p.value
        elif key< p.key:
            p = p.left
        else:
            p = p.right
# 노드를 삽입하는 add 함수 
def add(self, key:Any, value: Any) -> bool:

    def add_node(node: Node, key: Any, value: Any) -> None:
        if key ==node.key:
            return False
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value, None, None)
            else:
                add_node(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value, None, None)
            else:
                add_node(node.right, key, value)
        return True
        
        if self.root is None:
            self.root Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        