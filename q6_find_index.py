# 6. Find index in array for item. Given an array, and an element to search for return


# take in array, number to find and a counter i
def findIndex(arr, number, index):
    # if the array index is equal to the 5
    if arr[0] == number:
        # return the the index
        return index
    else:
        # counting what index we are
        index = index +1
        #print(i)
        return findIndex(arr[1:], number, index)

# array of values
arr = [3, 4, 5, 6, 7]

# counter
index=0

# number to find
number = 5

# call the function
ans =findIndex(arr,number, index)
# print
print (ans)
