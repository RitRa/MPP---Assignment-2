# 2. Product of an array Given an array of numbers return it’s product (all the numbers
#multiplied together).


 # using recursion
 #take in the array and N the length
def findproduct(arr, N):
    # if the length of the array is equal to one
    if len(arr)== 1:
        # print the one element
        return arr[0]
    else:
        # take the first element and multiple it to each element
        return arr[0] *findproduct(arr[1:], N)


# input values to list
arr = [3, 4, 5, 6, 7]

# calculating length of array
N = len(arr)

ans =findproduct(arr,N)
print (ans)
