from node import node

def main():

    head = node('T', None)    
    head = node('K', head)
    head = node('N', head)
    head = node('I', head)
    head = node('L', head)

    selection = head
    
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    
    selection.addNodeAfter('E')
    
    selection = selection.getLink()

    selection.addNodeAfter('D')

    selection = selection.getLink()

    selection.addNodeAfter('L')

    selection = selection.getLink()

    selection.addNodeAfter('I')

    selection = selection.getLink()

    selection.addNodeAfter('S')

    selection = node.listSearch(selection, 'I')

    tail = selection

    tail = node.listSearch(head, 'T')

    selection.removeNodeAfter()
    selection.removeNodeAfter()

    tail = None

    head.removeNodeAfter()
    head.removeNodeAfter()

    print(f'How many nodes does head contain? {node.listLength(head)}')
    print(f'How many nodes does selection contain? {node.listLength(selection)}')
    print(f'How many nodes does tail contain? {node.listLength(tail)}')

    if(node.listSearch(head,'K')):
        print('Head contains the letter K')

    if(node.listSearch(selection,'I')):
        print('Selection contains the letter I')

    copy = node.listCopyWithHead(head)
    print(f'copy[0] contains {node.listLength(copy[0])} nodes')
    print(f'copy[1] contain {node.listLength(copy[1])} nodes')

    print(f'First node in copy[0] contains {copy[0].getData()}')
    print(f'First node in copy[1] contains {copy[1].getData()}')


    i = 1
    while i <= 10:
        
        if (head.listPosition(head, i) != None):
            print(f'head contains position {i}')
        else:
            print(f'Head does not contain position {i}')

        i+=1

if __name__ == "__main__":
    main()