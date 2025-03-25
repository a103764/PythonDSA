# normal search

# Unordered Linear Search: search from front till find
def search(unorderedList, term):

    for i, item in enumerate(unorderedList):
        
        if term == item:
            return i
    return None



# Ordered Linear Search: search from front, but if term more than item, no need search more
def searchOrdered(orderedList, term):
    
    for i in range(len(orderedList)):

        if term == orderedList[i]:
            return i
        elif orderedList[i] > term:
            return None
        


# Ordered Binary Search (iterative) = O(logn) - O(n)
def BinarySearchIterative(orderedList, term):
    idxFirstElement = 0
    idxLastElement = len(orderedList) - 1

    while idxFirstElement <= idxLastElement:

        midpoint = (idxFirstElement + idxLastElement) // 2

        # check term at midpoint
        if orderedList[midpoint] == term:
            return midpoint

        # check if term is greater than midpoint, then firstIdx = midpoint + 1
        if term > orderedList[midpoint]:
            idxFirstElement = midpoint + 1
        else:
            idxLastElement = midpoint - 1

        # stop once first pointer crosses last pointer
        if idxFirstElement > idxLastElement:
            return None 
        


def BinarySearchRecursive()




mylist = [60, 1, 88, 10, 11, 600]
myOrderedList = [2, 3, 4, 6, 7, 9]

# idx = search(mylist, 11)
# print(idx)

# idx = searchOrdered(myOrderedList, 4)
# print(idx)

idx = BinarySearchIterative(myOrderedList, 7)
print(idx)

print('test')