class Queue:
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
        self.__first_node = None
        self.__last_node = None

    def add(self, item):
        new_node = self.Node(item)
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = self.__first_node
        else:
            self.__last_node.set_next(new_node)
            self.__last_node = new_node

    def remove(self):
        try:
            data = self.__first_node.get_data()
            self.__first_node = self.__first_node.get_next()
            return data
        except Exception as e:
            print("NoSuchElementException", e)

    def element(self):
        try:
            return self.__first_node.get_data()
        except Exception as e:
            print("NoSuchElementException", e)

    def peek(self):
        return self.__first_node.get_data()

    def is_empty(self):
        if self.__first_node is None:
            return True
        else:
            return False
