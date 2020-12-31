from BTreeNode import BTreeNode
class BTree:
    def __init__(self, minDegree: int):
        self.minDegree = minDegree
        self.root = BTreeNode(minDegree)

    def search(self, key: int):
        return self.__searchAux(key, self.root)

    def __searchAux(self, key: int, searching: BTreeNode):
        i = 0
        while i < searching.numberOfKeys and key > searching.valueKey[i]:
            i += 1
        if i < searching.numberOfKeys and key == searching.valueKey[i]:
            return searching, i
        elif searching.leaf:
            return None
        else:
            return self.__searchAux(key, searching.children[i])

    def __splitChild(self, parent: BTreeNode, toSplitIndex: int):
        nearLeaf = BTreeNode(self.minDegree)
        toSplitNode: BTreeNode = parent.children[toSplitIndex]
        nearLeaf.leaf = toSplitNode.leaf
        nearLeaf.numberOfKeys = self.minDegree - 1

        for i in range(self.minDegree - 1):
            nearLeaf.valueKey[i] = toSplitNode.valueKey[i + self.minDegree]

        if not toSplitNode.leaf:
            for j in range(self.minDegree):
                nearLeaf.children[j] = toSplitNode.children[j + self.minDegree]
        toSplitNode.numberOfKeys = self.minDegree - 1

        for i in range(parent.numberOfKeys, toSplitIndex, -1):
            parent.children[i + 1] = parent.children[i]
        parent.children[toSplitIndex + 1] = nearLeaf

        for i in range(parent.numberOfKeys - 1, toSplitIndex - 1, -1):
            parent.valueKey[i + 1] = parent.valueKey[i]
        parent.valueKey[toSplitIndex] = toSplitNode.valueKey[self.minDegree - 1]
        parent.numberOfKeys += 1

    def __insertNonFull(self, toInsertIn: BTreeNode, key: int):
        i = toInsertIn.numberOfKeys - 1
        if toInsertIn.leaf:
            while i >= 0 and key < toInsertIn.valueKey[i]:
                toInsertIn.valueKey[i + 1] = toInsertIn.valueKey[i]
                i -= 1
            toInsertIn.valueKey[i + 1] = key
            toInsertIn.numberOfKeys += 1
        else:
            while i >= 0 and key < toInsertIn.valueKey[i]:
                i -= 1
            i += 1
            if toInsertIn.children[i].numberOfKeys == 2 * self.minDegree - 1:
                self.__splitChild(toInsertIn, i)
                if key > toInsertIn.valueKey[i]:
                    i += 1
            self.__insertNonFull(toInsertIn.children[i], key)

    def insert(self, key):
        root = self.root
        if root.numberOfKeys == 2 * self.minDegree - 1:
            newRoot = BTreeNode(self.minDegree)
            newRoot.leaf = False
            newRoot.numberOfKeys = 0
            newRoot.children[0] = root
            self.root = newRoot
            self.__splitChild(newRoot, 0)
            self.__insertNonFull(newRoot, key)
        else:
            self.__insertNonFull(root, key)

    def preOrder(self):
        self.__preOrderAux(self.root, "")

    def __convertKeysToString(self, node: BTreeNode):
        keysString = ""
        for i in range(node.numberOfKeys):
            keysString += str(node.valueKey[i]) + " "
        return keysString

    def __preOrderAux(self, root: BTreeNode, initialString: str):
        if root is None:
            return
        allKeysString = self.__convertKeysToString(root)
        print(initialString + allKeysString)
        for i in range(root.numberOfKeys + 1):
            self.__preOrderAux(root.children[i], initialString + " " * (len(allKeysString) - 1))

    def inOrder(self):
        orderedList = []
        self.__inOrderAux(self.root, orderedList)
        listString = ""
        for key in orderedList:
            listString += str(key) + " "
        print(listString)

    def __inOrderAux(self, node: BTreeNode, orderedList: [int]):
        if node is None:
            return
        for i in range(node.numberOfKeys):
            self.__inOrderAux(node.children[i], orderedList)
            orderedList.append(node.valueKey[i])

        self.__inOrderAux(node.children[node.numberOfKeys], orderedList)