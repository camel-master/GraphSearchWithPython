#from collections import deque
from Stack import Stack
from Queue import Queue


def visit(n):
    print(n.data, end=' ')


def dfs_recursive(node):
    if not node:
        pass
    node.marked = True
    visit(node)
    for n in node.adjacent:
        if not n.marked:
            dfs_recursive(n)


class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            self.marked = False
            self.adjacent = []

    def __init__(self, arr):
        self.__nodes = []
        for data in arr:
            self.newNode = self.Node(data)
            self.__nodes.append(self.newNode)

    def add_edge(self, i1, i2):
        n1 = self.__nodes[i1]
        n2 = self.__nodes[i2]
        if not (n2 in n1.adjacent):
            n1.adjacent.append(n2)
        if not (n1 in n2.adjacent):
            n2.adjacent.append(n1)

    """
    #Implement stack by python list type
    def dfs(self, index):
        root = self.__nodes[index]
        stack = [root]
        root.marked = True
        while len(stack) > 0:
            pop_node = stack.pop()
            for n in pop_node.adjacent:
                if not n.marked:
                    n.marked = True
                    stack.append(n)
            visit(pop_node)
        print()
    """

    def dfs(self, index):
        root = self.__nodes[index]
        stack = Stack()
        stack.push(root)
        root.marked = True
        while not stack.is_empty():
            pop_node = stack.pop()
            for n in pop_node.adjacent:
                if not n.marked:
                    n.marked = True
                    stack.push(n)
            visit(pop_node)
        print()

    def dfs_recursive_first(self, index):
        dfs_recursive(self.__nodes[index])
        print()

    '''
    # use queue data structure with python dequeue library
    def bfs(self, index):
        root = self.__nodes[index]
        queue = deque()
        queue.append(root)
        root.marked = True
        while len(queue) > 0:
            pop_node = queue.popleft()
            for n in pop_node.adjacent:
                if not n.marked:
                    n.marked = True
                    queue.append(n)

            visit(pop_node)
        print()
    '''

    def bfs(self, index):
        root = self.__nodes[index]
        queue = Queue()
        queue.add(root)
        root.marked = True
        while not queue.is_empty():
            remove_node = queue.remove()
            for n in remove_node.adjacent:
                if not n.marked:
                    n.marked = True
                    queue.add(n)

            visit(remove_node)
        print()
