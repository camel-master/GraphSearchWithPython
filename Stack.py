class Stack:
    class Node:
        def __init__(self, data):
            self.__data = data
            self.__next = None

        def get_data(self):
            return self.__data

        def get_next(self):
            return self.__next

        def set_next(self, next_node):
            self.__next = next_node

    def __init__(self):
        self.__top_node = None

    def pop(self):
        try:
            temp = self.__top_node.get_data()
            self.__top_node = self.__top_node.get_next()
            return temp
        except Exception as e:
            print("Empty Stack Exception")

    def peek(self):
        try:
            return self.__top_node.get_data()
        except Exception as e:
            print("Empty Stack Exception")

    def push(self, item):
        new_node = self.Node(item)
        new_node.set_next(self.__top_node)
        self.__top_node = new_node

    def is_empty(self):
        if self.__top_node is None:
            return True
        else:
            return False
