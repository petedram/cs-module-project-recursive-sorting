# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    #base case - what is a sub problem and stop recursion?
    if end >= start:
        # guess == target
        guess = arr[((start + end) //2)]
        if guess == target:
            return arr.index(guess)

        #how to get to base case - a sub problem.
        # if guess high, reduce middle by 1
        elif guess > target:
            #add recursive call reduce end by 1
            return binary_search(arr, target, start, end-1)

        else:
            #add recursive all increase start by 1
            return binary_search(arr, target, start + 1, end)

    else:
            return -1 #not found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    from sorting import merge_sort
    maximum = 7
    elements = maximum + 1 #need to find the max value + 1
    assign = [0] * elements #new array of zeros
    print(f'assign first: {assign}')


    #what index is each num in array
    i = 0
    while i < len(assign): #redo this...
        print(f'put value of array = {arr[i]} into index of assign = {i}')
        assign.insert(i, arr[i])
        i+=1
    
    print(f'assign second: {assign}')


    sorted = merge_sort(arr)
    print(sorted)

    start = 0
    end = len(sorted)-1
    new_index = binary_search(sorted, target, start, end)

    return new_index


print(agnostic_binary_search([1, 7, 5, 4, 0], 5))