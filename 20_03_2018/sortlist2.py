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

if __name__== '__main__':
    list = [l for l in range(10000000)] # geraçao automatica da lista
    vlr = 999900
    print('Linear:',linear_search(list,vlr))
    print('Encontrou: ',binary_search(list,vlr))
    #print(mylist)