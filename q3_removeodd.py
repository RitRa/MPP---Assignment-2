# 3. Remove all odd numbers Given an array of numbers return an array with all the
#odd numbers removed.

# using recursion.
# take in the array
def removeOdd(arr):
    if not arr:
        return []
    # use modulus to check whether is it an odd number, if it leaves a remainder
    if arr[0] % 2 == 1:
        # return odd number and continue recursion
        return [arr[0]] + removeOdd(arr[1:])
    return removeOdd(arr[1:])




# input values to list
arr = [3, 4, 5, 6, 7]

print(removeOdd(arr))
