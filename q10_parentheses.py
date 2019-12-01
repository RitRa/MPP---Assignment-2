#Verify the parentheses Given a string, return true if it is a nesting of zero or more
#pairs of parenthesis, like “(())” or “((()))”.

def check(string, counter=0):
  if not string:
    return "Balanced" if counter == 0 else "Unbalanced"
  # if counter is less than 1 it is unbalnaced
  elif counter < 0:
    return "Unbalanced"
  # if the char is (
  elif string[0] == "(":
    # continue recursion and add to 1 to counter
    return check(string[1:], counter+1)
  # checks the next char is )
  elif string[0] == ")":
      # continues recursion and subtracts 1 from counter
    return check(string[1:], counter-1)
  else:
    return check(string[1:], counter)

# string to check
string ="(())"

# call the function
print(check(string))
