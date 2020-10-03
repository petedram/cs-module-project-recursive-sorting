# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements #new array of zeros

    # Your code here
    l = 0 #left index
    r = 0 #right index
    m = 0 #merged index

    #merge 2 sorted lists together, smallest at front
            #single lists: then smallest will always be at the front
            #pairs list: compare first in each pair, smallest goes first
            #4 list: don't have to check evey element because know sub-arrays are already sorted.
                #check the front of each one to find smallest
                #repeat for each sub-array i.e. 1 vs 2
                #when one of the sub-arrays is empty, put remaining of other sub-array to end of merged piece (left to right)
            #8 list etc: repeat until single list..

    while l < len(arrA) and r < len(arrB):
        if arrA[l] <= arrB[r]:
            merged_arr[m] = arrA[l]
            # print(f'putting {arrA[l]} first')
            l+=1
        else:
            merged_arr[m] = arrB[r]
            # print(f'putting {arrB[r]} first')
            r+=1

        m+=1
    
    while l < len(arrA):
        merged_arr[m]=arrA[l]
        l+=1
        m+=1
    
    while r < len(arrB):
        merged_arr[m]=arrB[r]
        r+=1
        m+=1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    #base case
    #single list, no more sub-arrays
    if len(arr) <=1:
        return arr
    
    
    #move towards base-case as a subset problem
    #divide in half until subarrays of 1
    midpoint = len(arr) //2
    lhs = merge_sort(arr[:midpoint]) #left hand side
    rhs = merge_sort(arr[midpoint:]) #right hand side

    #invoke merge here?
    #this will be on the way back up... after split
    return merge(lhs, rhs)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# print(merge_sort([1, 5, 8, 4]))

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
