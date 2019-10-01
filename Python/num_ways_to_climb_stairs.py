"""
Solution to numbers of ways to climb stairs given number of stairs
and you can climb one or two steps at a time.
"""

def staircase_dp(n):
    """
    This is a DP solution to the problem. 
    We solve for each of the sub problem my looking at the ways
    for a step - 1 and step -2.
    This solution is actually solving for Fibonacci series.
    Another approach is provided below (staircase_fib) with direct Fibonacci solution.
    """
    if n <= 1:
        return 1
    steps = [0] * (n + 1)
    steps[1] = 1
    steps[2] = 2

    for step in range(3, n+1):
        steps[step] = steps[step-1] + steps[step - 2]


    return steps[-1]

def staircase_fib(n, look_up = {0:1, 1:1}):
    """
    Num of ways for 1 step - 1                                   (1)
    Num of ways for 2 steps - 2, 1                               (2)
    Num of ways for 3 steps - 1 1 1, 2 1, 1 2                    (3)
    Num of ways for 4 steps - 1 1 1 1, 2 2, 1 1 2, 2 1 1, 1 2 1  (5)
    and so on....
    So the sequence we get is 1, 2, 3, 5, ..... which actually is the 
    Fibonacci series.
    This method uses a dictonary as cache/lookup table to store all the 
    calculated Fibonacci nth term.
    """
    if n in look_up:
        return look_up[n]
    else:
        look_up[n] = staircase_fib(n-1) + staircase_fib(n-2)
    return look_up[n]

print (staircase_dp(4))
# 5
print (staircase_dp(5))
# 8
print (staircase_fib(5))
# 8
print (staircase_fib(2))
# 2
