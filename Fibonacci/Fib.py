def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else: 
        return fib(n-1) + fib(n - 2)


def fib_by_storing(n, memo):
    '''
    if n is in memoise, return memoise[n]
    # whenever we encounter the same n being called, we access it
    else:
        memoise[n] = fib(n-1) + fib(n-1)
        return memoise[n]
    '''
    if n in memo:
        return memo[n]
    elif n == 2:
        memo[n] = 1
    elif n == 1:
        memo[n] = 0
    else: 
        memo[n] = fib_by_storing(n-1, memo) + fib_by_storing(n-2, memo)
    return memo[n]




# Iterative solution

# start with an array: [0, 1]

# keep track of how many fib operations we've done

def iterative_fib(n):
    my_list = [0,1]
    count_of_operations = 0
    while count_of_operations is not n:
        temp_val = my_list[0]
        my_list[0] = my_list[1]
        my_list[1] = temp_val + my_list[1] 
        count_of_operations += 1
    return my_list[1]

for i in range(7):
    print(iterative_fib(i))
    
    

