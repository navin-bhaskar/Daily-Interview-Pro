"""                     Shree Krishnaya Namaha              """

high_prec_ops = "*/"
low_prec_ops = "+-"
parens = "()"
all_ops = high_prec_ops + low_prec_ops + parens

class Solution:
    
    def calculate(self, s):
        """https://leetcode.com/problems/basic-calculator/"""
        post_fix = self._infix_to_postfix_(s)
        return self._eavl_postfix_(post_fix)

    def _eavl_postfix_(self, postfix):
        eval_ret = 0
        data_stack = []
        for token in postfix:
            if token in all_ops:
                if len(data_stack) < 2:
                    return Exception("Not enough args")
                else:
                    val1 = int(data_stack.pop())
                    val2 = int(data_stack.pop())
                    if token == "+":
                        data_stack.append(val1+val2)
                    elif token == "-":
                        data_stack.append(val2-val1)
                    elif token == "*":
                        data_stack.append(val1*val2)
                    elif token == "/":
                        if val2 == 0:
                            raise Exception("Divide by zero exception")
                        data_stack.append(val1//val2)
            else:
                data_stack.append(token)

        if data_stack:
            eval_ret = data_stack[-1]
        else:
            eval_ret = 0

        return eval_ret            

    def _infix_to_postfix_(self, expr):
        postfix = []
        num = []
        op_stk = []
        for token in expr:
            if token == " ":
                if num:
                    postfix.append("".join(num))
                    num.clear()
            elif ord(token) >= ord("0") and ord(token) <= ord("9"):
                num.append(token)
            elif token in all_ops:
                if num:
                    postfix.append("".join(num))
                    num.clear()
                if token != ")" and (len(op_stk) == 0 or op_stk[-1] == "("):
                        op_stk.append(token)
                elif token in low_prec_ops:
                    while op_stk and op_stk[-1] != "(":
                        postfix.append(op_stk.pop())
                    op_stk.append(token)
                elif token in high_prec_ops:
                    postfix.append(token)
                elif token == "(":
                    op_stk.append("(")
                elif token == ")":
                    while op_stk and op_stk[-1] != "(":
                        postfix.append(op_stk.pop())
                    if op_stk:
                        op_stk.pop()
                    else:
                        print ("Error, unbalance bracket")
                        return
            else:
                print ("Unrecognized token")
                return

        if num:
            postfix.append("".join(num))
            num.clear()

        while op_stk:
            if op_stk[-1] == ")":
                op_stk.pop()
            elif op_stk[-1] == "(":
                op_stk.pop()
            else:
                postfix.append(op_stk.pop())

        return postfix

                    
sol = Solution()
#print (sol.calculate('2-1+2'))
#print (sol.calculate("(1+(4+5+2)-3)+(6+8)"))
#print (sol.calculate("(1)"))
print (sol.calculate("(3)+1"))