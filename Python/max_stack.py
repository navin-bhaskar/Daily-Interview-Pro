"""                 Shree Krishnay Namaha               """

class MaxStack(object):

    def __init__(self):
        self._stk = []
        self._max = float("-inf")
        self._max_idx = 0

    def push(self, item):
        if item > self._max:
            self._max = item
            self._max_idx = len(self._stk)
        self._stk.append((self._max_idx, item))

    def __is_empty(self):
        return len(self._stk) == 0

    def pop(self):
        if self.__is_empty():
            return None
        return self._stk.pop()[1]

    def max(self):
        if self.__is_empty():
            return None
        return self._stk[self._stk[-1][0]][1]

def main():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print (s.max())
    # 3
    s.pop()
    s.pop()
    print (s.max())
    # 2

if __name__ == "__main__":
    main()