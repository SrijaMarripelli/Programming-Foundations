# Search for an item in an ordered list
# This technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarySearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # Start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        pass
        # TODO : Calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # TODO : If item is found, return the index
        if itemlist[midPt] == item:
            return midPt

        # TODO : Otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1


    if lowerIdx > upperIdx:
        return None
    

print(binarySearch(23, items))
print(binarySearch(87, items))
print(binarySearch(250, items))