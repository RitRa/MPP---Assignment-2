#8. Print an array Given an array of integers prints all the elements one per line. This
#is a little bit different as there is no need for a ’return’ statement just to print and
#recurse.

 # using recursion.
def printArr(arr, N):
    # stopping the recursion when it gets to 0
    if len(arr)== 0:
        return True
    else:
        # print value
        print(arr[0])
        # continue recursion
        printArr(arr[1:], N)


# array of values
arr = [3, 4, 5, 6, 7]

# calculating length of array
N = len(arr)+1

# call the funtion
ans =printArr(arr,N)
# print
print (ans)
