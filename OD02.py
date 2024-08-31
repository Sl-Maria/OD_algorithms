class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(11)
queue.enqueue(22)
queue.enqueue(33)
print(queue.size())
print(queue.dequeue())
print(queue.size())

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

root = Node(70)
root = root.insert(root, 50)
root = root.insert(root, 90)
root = root.insert(root, 30)
root = root.insert(root, 60)
root = root.insert(root, 80)
root = root.insert(root, 100)
root = root.insert(root, 20)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        else:
            self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()