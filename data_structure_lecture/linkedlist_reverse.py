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
        ptr = self.head
        while ptr != None:
            print(ptr.data, end=" ")
            ptr = ptr.next

    def reverse(self):
        ptr = self.head
        tail = None
        while ptr != None:
            temp = ptr.next
            ptr.next = tail
            tail = ptr #while 탈출 직전 tail이 역순 연결 리스트의 head가 된다.
            ptr = temp

        self.tail = self.head
        self.head = tail

T = int(input())

for _ in range(T):
    linkedList = LinkedList()
    N = int(input())
    for _ in range(N):
        data = int(input())
        linkedList.insertNode(data)

    linkedList.reverse()
    linkedList.printLinkedList()