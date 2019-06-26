'''

Step 1: Find the middle number
Step 2: Assign Left to the leftmost index, 
Right to the rightmost

M = (Sum of Left + Right) / 2

e.g with a list of 10 elements, L = 0, R = 9
(0 + 9)// 2 = 4 (floored)

'''

def findValue(input_list, target_value):
    right = len(input_list) - 1
    left = 0
    mid = (right + left) // 2 
    while right > left and input_list[mid] != target_value:
        if target_value > input_list[mid]:
            left = mid
            mid = (right + left) // 2 
        elif target_value < input_list[mid]:
            right = mid
            mid = (right + left) // 2 
        else: 
            if input_list[mid] == target_value:
                return mid
            else:
                return "Not there"

print(findValue([1,2,3,4,5,6,7,8,9], 11))



# RECURSIVE IMPLEMENTATION: O(Log(n)) time | O(Log(n)) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
        # base case: is the left pointer greater than the right?
        # if so, we're done.
    if left > right:
        return -1 # or whatever signifies 'not found'
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle # we return the middle because that's where we found the item
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle-1)
        # we are cutting out the right half of the array, so the right pointer
        # is one position left of the middle.
    else: 
        return binarySearchHelper(array, target, middle+1, right)



# ITERATIVE SOLUTION O(log(n)) time | O(1) space

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
        # base case: is the left pointer greater than the right?
        # if so, we're done.
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else: 
            left = middle + 1
    return -1
    
