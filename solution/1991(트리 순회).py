import sys
input = sys.stdin.readline

def postorder(tree,node,visit):
    if (tree[node][0] != '.'):
        postorder(tree, tree[node][0], visit)
    if (tree[node][1] != '.'):
        postorder(tree, tree[node][1], visit)
    visit.append(node)

def inorder(tree,node,visit):
    if(tree[node][0] != '.'):
        inorder(tree, tree[node][0], visit)
    visit.append(node)
    if (tree[node][1] != '.'):
        inorder(tree, tree[node][1], visit)

def preorder(tree,node,visit):
    visit.append(node)
    if (tree[node][0] != '.'):
        preorder(tree, tree[node][0], visit)
    if (tree[node][1] != '.'):
        preorder(tree,tree[node][1], visit)

if __name__ == '__main__':
    n = int(input())
    tree = {}

    for _ in range(n):
        # parent left_child right_child
        a,b,c = input().strip().split(' ')
        tree[a] = [b,c]

    visit = []
    preorder(tree, 'A', visit)
    print(''.join(visit))

    visit=[]
    inorder(tree, 'A', visit)
    print(''.join(visit))

    visit=[]
    postorder(tree, 'A', visit)
    print(''.join(visit))