# 4. Remove all even numbers Given an array of numbers return an array with all the even numbers removed.


# using recursion.
# take in the array
def removeOdd(arr):
    if not arr:
        return []
    # use modulus to check whether is it aan even number, if it leaves a remainder of 0
    if arr[0] % 2 == 0:
        # return even number and continue recursion
        return [arr[0]] + removeOdd(arr[1:])
    return removeOdd(arr[1:])




# input values to list
arr = [3, 4, 5, 6, 7]

# print and call function
print(removeOdd(arr))
