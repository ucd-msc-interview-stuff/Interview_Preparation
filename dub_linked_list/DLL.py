'''

A doubly linked list has a head and a tail. 

The head is the first element, the tail the last,
though this can be the opposite depending on implementation. 
It doesn't matter so long as you're consistent. 



Each node has a link to the node ahead of it and the 
one behind it. 


'''

class DoublyLinkedList:

    def __init__(self):
        # Each node has a head and a tail
        self.head = None
        self.tail = None 


    def remove(self, node):
        '''
        two edge cases:
        - are we dealing with the head
        - are we dealing with the tail
        '''
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        

    def removeNodesWithValue(self, value):
        '''
        A combination of searching and removal

        '''

        node = self.head
        while node is not None:
            nodeToRemove = node
            # we store node.next as node so that we have somewhere to go to next
            node = node.next
            if nodeToRemove.value == value:
                # this will delete our pointers, so we can't just remove node
                self.remove(nodeToRemove)
                
            





    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        # if we break, either node is none, or we've found the value
        return node is not None
        # this will either be true if we found it, or false if we didn't
    
    def removeNodeBindings(self, node):
        # update the pointers of the surrounding nodes
        # update the pointers of the given nodes

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None