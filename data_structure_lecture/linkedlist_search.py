import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def printLinkedList(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

N = int(input())
linkedList = LinkedList()

for _ in range(N):
    data = int(input())
    linkedList.insertNode(data)

linkedList.printLinkedList()
