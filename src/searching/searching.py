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
    pass
