"                   Shree Krishnaya Namaha                  "

class Solution:
  def isValid(self, s):
    parens = {")": "(", "}": "{", "]": "["}
    if not s:
        return True

    theStack = []

    for char in s:
        if char in parens:
            if theStack:
                item = theStack.pop()
                if item is not parens[char]:  # Not a matching pair
                    return False
            else:
                return False
        elif char in parens.values():
            theStack.append(char)
        else:
            return False        # Bad char
    
    if theStack:
        return False      # not balanced
    else:
        return True


# Test Program
s = "()(){(())" 
# should return False
#print(Solution().isValid(s))
assert Solution().isValid(s) == False

s = ""
# should return True
#print(Solution().isValid(s))
assert Solution().isValid(s) == True

s = "([{}])()"
# should return True
#print(Solution().isValid(s))
assert Solution().isValid(s) == True