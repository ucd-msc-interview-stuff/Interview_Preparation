class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # 1. check if the value is going left or right
        if value < self.value:
            # if the val is smaller, we're going left
            # first check if there's already a node there
            if self.left is None:
                # if not, add it
                self.left = BST(value)
            else:
                # if there's no space, we run the same process on the child node
                self.left.insert(value)
        else:
            # this means the value is the same or larger, so we go right
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        # this final return is just for testing, it allows us to chain methods together
        return self

    def contains(self, value):
        '''
        The insert function is recursive, but you can descend through the tree 
        iteratively too. We'll do that here by tracking the current node
        and using a while loop. You can do the same thing for the insert method.
        '''
        current = self

     # once we hit None it means we're out of nodes
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                # they're the same!
                return True
        return False

    def delete(self, value, parent=None):
        '''
        There are several different possibilities when it comes to delete:
        1) We're deleting a node that has no children
        2) We're deleting a node that has one child 
        3) We're deleting a node that has two children (and therefore need to rebalance the tree)
        We keep track of the parent node, because if we want to chop off a branch we're going to have to connect 
        the subnodes of the one we're deleting to the parent above it.
        We'll take the iterative approach again, and the start of the method
        is very similar to contains, since we have to find the node to delete it...
        '''

        # SEARCH FOR IT
        current = self

        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
                continue
            elif value > current.value:
                parent = current
                current = current.right
                continue

            # ok we found it, now KILL IT
            else:
                # first check if there are two children
                if current.left is not None and current.right is not None:

                    '''
                    If we want to delete a node that has two children, the rule is this:
                    FIND THE SMALLEST VALUE IN THE RIGHT SUBTREE. That's the one that's got to go where we are
                   '''
                    current.value = current.right.getMinValue()
                    '''
                    We then have to run through the same process recursively. 
                    This will do the tree balancing
                    we are now trying to remove the value to the right of where we currently are
                    '''
                    current.right.delete(current.value, current)

                    '''
                    at this point we need to consider what happens if we're deleting the root
                    i.e what if there is no parent node? 
                    The elifs below rely on there being a parent node... we need to check 
                    '''
                elif parent is None:
                    if current.left is not None:
                        # the single child is to the left, so we simply chop it out and reattach
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else: 
                        # this means we're deleting the root and it has no children
                        # it's a weird edge case
                        current.value = None
                # now what about if the one we're deleting has only one child?

                # this means we went left
                elif parent.left == current:
                    # if we went left, we go for the left again, unless it doesn't exist, in which case we go to the right
                    parent.left = current.left if current.left is not None else current.right
                # and vice versa
                elif parent.right == current:
                    parent.right = current.left if current.left is not None else current.right

                break
            return self


    # we need this method for the delete
    def getMinValue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value
