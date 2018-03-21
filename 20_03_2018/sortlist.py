def linear_search(mylist, find):
    for x in mylist:
        if x == find:	
            return True
    return False


def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist))//2
        print('O mid é {}'.format(mid))
        if mylist[mid] == find:
            print('O número {} encontrado!'.format(find))
            return True
        elif find < mylist[mid]:
            print('O número está à esquerda da lista {}!'.format(mylist))
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
            print('O número está à direita da lista {}! {}'.format(mylist,mid))
    return False
if __name__ == '__main__':
    list = [x + 1 for x in range (100)]
    linear_search(list, 19)
    binary_search(list, 19)