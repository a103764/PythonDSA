# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 08:48:49 2025

@author: A103764
"""

#%% stack implementation using arrays 
size = 3
data = [0]*(size)

# stack empty
top = -1

# push to top 
def push(x):
    
    # need to declare as global
    global top
    
    if top >= size -1:
        print("stack overflow")
        
    else: 

        top = top + 1
        data[top] = x
        
        print(data)

# remove from top    
def pop():
    
    global top

    if top == -1:
        print("Stack underflow")
    else:
        data[top] = 0
        top = top - 1
        return data[top]

def peak():
    global top

    if top == -1:
        print("stack empty")
    else:
        print(data)



# FILO
#push("egg")
#push("ham")
#push("spam")
#pop()
#peak()
#pop()
#peak()


#%% stack implementation using linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class StackUsingLL:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):

        if self.top:
            data = self.top.data
            self.size -= 1

            # check if there more than one item
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            print("stack is empty")


    def printAll(self):
        current = self.top

        while current:
            print(current.data)
            current = current.next

words = StackUsingLL()
words.push("egg")
words.push("ham")
words.pop()
words.push("spam")
words.pop()

# display last item
words.printAll()

#%% Ques

