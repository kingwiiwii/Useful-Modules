''' Sort a list of IPs '''
def ipSort(ListOfIPs):
    toSort = []
    toSort = ListOfIPs
    for i in range(len(toSort)):
        toSort[i] = "%3s.%3s.%3s.%3s" % tuple(toSort[i].split("."))
        toSort.sort()
    for i in range(len(toSort)):
        toSort[i] = toSort[i].replace(" ", "")
    return toSort