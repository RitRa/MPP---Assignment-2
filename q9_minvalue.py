#9. Find the minimum element in an array of integers. You can carry some extra
#information through method arguments such as minimum value.

 # using recursion.
def findMin(arr):
    if len(arr) == 1:
       return arr[0]
    else:
       # return the min value
       return min(arr[0], findMin(arr[1:]))



# array of values
arr = [3, 4, 5, 6, 7]

# call the funtion
ans =findMin(arr)
# print
print (ans)
