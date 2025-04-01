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
        


def BinarySearchRecursive(orderedList, firstIdx, lastIdx, term):

    if firstIdx > lastIdx:
        return None
    
    else:

        midpoint = firstIdx + (lastIdx - firstIdx) // 2

        # check midpoint value with left and right
        if orderedList[midpoint] > term:
            return BinarySearchRecursive(orderedList, firstIdx, midpoint -1, term)

        elif orderedList[midpoint] < term:
            return BinarySearchRecursive(orderedList, midpoint + 1, lastIdx, term)

        else:
            return midpoint 
        


def nearestMid(inputList, lowIdx, uppIdx, searchValue):
    
    var2 = (uppIdx - lowIdx) // (inputList[uppIdx] - inputList[lowIdx])
    var3 = searchValue - inputList[lowIdx]
    
    mid = lowIdx + var2 * var3
    
    return mid

def interpolation_search(orderedList, term):

    lowerIdx = 0 
    upperIdx = len(orderedList) - 1

    # safety 1 
    while lowerIdx < upperIdx:

        midpoint = nearestMid(orderedList, lowerIdx, upperIdx, term)

        # safety 2 
        if midpoint > upperIdx or midpoint < lowerIdx:
            return None
        
        elif orderedList[midpoint] == term:
            return midpoint
        
        elif term > orderedList[midpoint]:
            lowerIdx = midpoint + 1

        else:
            upperIdx = midpoint - 1
    
    return None


def ExponentialSearch(orderedList, term):

    if orderedList[0] == term:
        return 0
    
    idx = 1

    # till conditions mentioned, move right exponentially
    while idx < len(orderedList) and orderedList[idx] < term:
        idx *= 2

    return BinarySearchRecursive(orderedList, idx // 2, min(idx, len(orderedList) - 1), term)

    return None
        






mylist = [60, 1, 88, 10, 11, 600]
myOrderedList = [2, 3, 4, 6, 7, 9]

# idx = search(mylist, 11)

# idx = searchOrdered(myOrderedList, 4)

# idx = BinarySearchIterative(myOrderedList, 7)

# idx = BinarySearchRecursive(myOrderedList, 0, len(myOrderedList) -1, 9)

# idx = interpolation_search(myOrderedList, 4)

idx = ExponentialSearch(myOrderedList, 9)
print(idx)

print('test')