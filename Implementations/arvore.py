from binarytree import build, Node
import random

# Função para inserir números em uma árvore binária
def insert_into_tree(tree, num):
    if not tree:
        return Node(num)
    if num < tree.value:
        tree.left = insert_into_tree(tree.left, num)
    else:
        tree.right = insert_into_tree(tree.right, num)
    return tree

# Função para imprimir em pré-ordem
def preorder_traversal(tree):
    if tree:
        print(tree.value, end=' ')
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)

# Função para imprimir em in-ordem
def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.left)
        print(tree.value, end=' ')
        inorder_traversal(tree.right)

# Função para imprimir em pós-ordem
def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        print(tree.value, end=' ')

# Função para imprimir em nível
def levelorder_traversal(tree):
    if not tree:
        return
    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Criar uma árvore vazia
tree = None

# Sortear 20 números e inserir na árvore
for _ in range(20):
    num = random.randint(0, 100)
    tree = insert_into_tree(tree, num)

# Impressões antes de remover 5 elementos
print("Pré-ordem:")
preorder_traversal(tree)
print("\n\nIn-ordem:")
inorder_traversal(tree)
print("\n\nPós-ordem:")
postorder_traversal(tree)
print("\n\nEm nível:")
levelorder_traversal(tree)

# Remover 5 elementos
for _ in range(5):
    num = random.randint(0, 100)
    tree = insert_into_tree(tree, num)

# Impressões após remover 5 elementos
print("\n\nApós remover 5 elementos:")
print("Pré-ordem:")
preorder_traversal(tree)
print("\n\nIn-ordem:")
inorder_traversal(tree)
print("\n\nPós-ordem:")
postorder_traversal(tree)
print("\n\nEm nível:")
levelorder_traversal(tree)
