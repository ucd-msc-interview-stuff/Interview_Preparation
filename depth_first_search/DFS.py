'''
Time complexity = O(V nodes + E edges)

This is because we traverse every vertex V, but also repeat the process
for every edge E coming out of  a particular node. 

Space complexity: O(V)
We're storing an array holding V nodes, 
but also we're doing V recursive calls
'''

class Node:
    depth = 0
    # class var for depth 
    def __init__(self, name, height = 1):
        self.children = []
        self.name = name
        self.height = height
        if self.height > Node.depth:
            Node.depth = self.height

    def addChild(self, name):
        temp = Node(name, self.height+ 1)
        self.children.append(temp)
        return temp

    def depthFirstSearch(self, array=[]):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return (array,Node.depth)

    def testDepth(self):
        counter = 0
        if len(self.children) is not 0:
            return counter
        else:
            counter += 1
            for child in self.children:
                testDepth(child)
        

x = Node(1)
x.addChild(2)
x.addChild(5)





# x.addChild(5)
# x.addChild(7)



my_arr = x.depthFirstSearch()

print(my_arr)

'''
           1
       /   \   \
    2       5   7



'''