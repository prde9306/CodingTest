#이진검색 트리 구현하기 

from __future__ import annotations
from typing import Any, Type

class Node:
    def __ init__ (self, key: Any, value: Any, left: Node =None, right: Node=None):
       
        self.key = key
        self.value = value
        self.left = left
        self.right = right
class BinarySearchTree:
    def __ init__(self):
        self.root = None
    
