import random

from BTree import BTree


def test():
    tree1 = BTree(2)
    A = [3, 1, 4, 2, 5, 7, 6, 11, 15, 22, 35, 21]
    for key in A:
        tree1.insert(key)

    print("PREORDER: ")
    tree1.preOrder()
    print()
    print("INORDER: ")
    tree1.inOrder()
    print()
    areIN = [3, 6, 15, 0, 13]
    for key in areIN:
        found = tree1.search(key)
        if found is None:
            print("No se encontró el elemento", key)
        else:
            print("Elemento", key, "encontrado")

    tree2 = BTree(2)
    AScrambled = A.copy()
    random.shuffle(AScrambled)
    for key in AScrambled:
        tree2.insert(key)
    print()
    tree2.preOrder()
    print()

    randomElements = [random.randint(-100000, 100000) for _ in range(1000)]
    largeTree = BTree(6)
    for key in randomElements:
        largeTree.insert(key)
    largeTree.preOrder()

if __name__ == '__main__':
    test()