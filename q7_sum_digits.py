#Sum of Digits Given a whole, number such as 23, return the sum of the digits in the
#number i.e. 2 + 3 = 5. For this would be useful to convert the number to a string
#then break it apart into digits.


# using recursion.
# take in a number
def sumdigits(number):
    # if it is equal to 0, return
    if number == 0:
        return number
    else:
        # modulus of the number is added together
        return number%10 + sumdigits(number//10)


# number to break apart
number = 254

ans =sumdigits(number)
print (ans)
