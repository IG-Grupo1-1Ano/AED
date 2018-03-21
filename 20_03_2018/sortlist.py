def linear_search(mylist, find):
    for x in mylist:
        if x == find:	
            return True
    return False


def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist))//2
        if mylist[mid] == find:
            return True
        elif find < mylist[mid]:
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
    return False


mylist = [1, 2, 3, 4, 5, 6, 7]
find = [10, 12]