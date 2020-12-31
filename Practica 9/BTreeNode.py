class BTreeNode:
    def __init__(self, minDegree: int):
        self.numberOfKeys: int = 0
        self.leaf: bool = True
        self.valueKey: [int] = [None] * (minDegree * 2 - 1)
        self.children: [BTreeNode] = [None] * (minDegree * 2)