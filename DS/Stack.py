__author__ = 'Rahul'

#import copy module for making deep copies
import copy

from collections import deque
from queue import LifoQueue

class Stack:
    def __init__(self, initialiser = None, stack_base = "list"):
        self.__base_container = stack_base
        
        if initialiser is None:
            self.__size = 0 #Set the original size of Stack as zero. 
            
            '''
                First we will decide what base container we are going to use for our Stack implementation.
                We will make that choice according to the value of stack_base parameter.
            '''
            if stack_base in ["list", "deque", "lifo queue"]:
                #We choose the appropriate base container for our Stack 
                if stack_base = "list":
                    self.__stack = []
                elif stack_base = "deque":
                    self.__stack = deque()
                else:
                    self.__stack = LifoQueue()
            else:
                #The base container specified to be used as stack is invalid.
                #Raise an appropriate exception.
        else:
            '''
                A value other than None for initialiser parameter has been passed.
                The initialiser passed must be listable.  
            '''
            
            #Perform necessary checks on type of initialiser
            
            self.__size = len(initialiser) #Set the size of the stack to the size of initialiser
            
            if stack_base = "list":
                    self.__stack = list(initialiser)
                elif stack_base = "deque":
                    self.__stack = deque(list(initialiser))
                else:
                    self.__stack = LifoQueue(list(initialiser))

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
