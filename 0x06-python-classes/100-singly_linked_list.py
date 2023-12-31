#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new node.


        Args:
            data (int): The data of the new node.
            next_node (Node): The next node of the new Node.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get/set the data of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""
    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head:
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(value)
        else:
            self.__head = new_node

    def __str__(self):
        current = self.__head
        while current:
            print(current.data)
            current = current.next_node
        return ''
