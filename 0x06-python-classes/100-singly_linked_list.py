#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    def data(self):
        return self.__data

    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    def next_node(self):
        return self.__next_node

    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
