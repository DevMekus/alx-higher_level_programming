#!/usr/bin/python3
"""Classes for a singly-linked list & its Node."""


class Node:
    """A Node Class in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Inita new Node.
        Args:
            data (int): The Node Data.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter function for  the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter function for the Node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter function for the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node function"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly-linked list Class or Model"""

    def __init__(self):
        """Init a singlyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Class for the print()of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
