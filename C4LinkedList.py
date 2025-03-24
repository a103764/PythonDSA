# singly linked list

#%% encapsulate data in Node singly linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#%% -------------transverse full list O(n)---------- #
class SinglyLinkedListV1:
    # init pointers
    def __init__(self):
        self.head = None
        self.size = 0

    # pass in pointer and data
    def append(self, data):
        node = Node(data)

        # if list is empty
        if self.head is None:
            self.head = node
        else:
            current = self.head

            # check till current.next == one
            while current.next:
                current = current.next

            current.next = node

words = SinglyLinkedListV1()
words.append("egg")
words.append("ham")
words.append("spam")

current = words.head
while current:
    print(current.data)
    current = current.next


#%% ------------------ add elements to linked list ------------------------- #
# Node consist data and 2 pointers to node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    # append at start of list O(1)
    def appendStart(self, data):
        newNode = Node(data)
        
        # list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
        self.size += 1
    
    # O(1) - we already have tail pointer
    def appendEnd(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    # min O(1), max O(n)
    def appendAtLocation(self, data):
        newNode = Node(data)
        current = self.head
        prev = self.head

        # transverse current through list
        while current:

            # if got existing data in list
            if current.data == data:

                # update new node pointers
                newNode.prev = prev
                newNode.next = current

                # update prev and current pointed nodes
                prev.next = newNode
                current.prev = newNode

                self.size += 1


            prev = current
            current = current.next
        
 #%%  print linked list       
words = DoublyLinkedList()
words.appendEnd("egg")
words.appendEnd("ham")
words.appendEnd("spam")

words.appendAtLocation("ham")

current = words.head
while current:
    print(current.data)
    current = current.next


        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            



# %%
