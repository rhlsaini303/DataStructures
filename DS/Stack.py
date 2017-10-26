__author__ = 'Rahul'

#import copy module for making deep copies
import copy

class Stack:
    def __init__(self, initialiser = None):
        if initialiser is None:
            self.__stack = []
            self.__size = 0
        else:
            self.__stack = list(initialiser)
            self.__size = len(initialiser)

    def __print_stack(self, L):
        if L:
            print('#TOP#'.rjust(7))
            for i in L:
                print('->', i)
        else:
            print('#EMPTY Stack: Nothing to Show#')

    def push(self, elem):
        self.__stack.append(elem)
        self.__size += 1

    def pop(self):
        if self.__size is not 0:
            self.__size -= 1
            return self.__stack.pop()
        else:
            return None

    def top(self):
        return copy.deepcopy(self.__stack[self.__size - 1])

    def multipush(self, elemseq):
        for i in elemseq:
            self.push(i)

    def multipop(self, num):
        if self.__size is 0:
            return None
        else:
            poplist = []
            for i in range(num):
                popped_item = self.pop()
                if popped_item is not None:
                    poplist.append(popped_item)
                else:
                    break
            return poplist

    def show_stack(self, *, specified_depth = None):
        if (specified_depth is not None) and (0 <= specified_depth <= self.__size):
            self.__print_stack(self.__stack[ : -(specified_depth + 1) : -1])
        else:
            self.__print_stack(self.__stack[ : : -1])
