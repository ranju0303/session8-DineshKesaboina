# 1
def checker_wrapper():
    """This is wrapper function that checks if the length of the docstring is >= 50 characters

    Returns:
        function: docStringCounter
    """
    count = 50

    def docStringCounter(fn):
        """This function counts the number of characters in a given function's docstring

        Args:
            function: some function fn

        Returns:
            Boolean : Whether or not the number of characters in docstring >= 50
        """
        return len(fn.__doc__) >= count
    return docStringCounter

# 2


def fib_wrapper():
    """This is a wrapper function around the next fib function
    """
    def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
    fib_num = [fib(x) for x in range(22)]

    def nextFib(somenum):
        """This function gives the next fibonacci number given one fibonacci number

        Args:
            somenum (int): some fibonacci number

        Returns:
            int: The next fibonacci number
        """
        if somenum in fib_num:
            idx = fib_num.index(somenum)
            return fib_num[idx + 1]
        else:
            raise ValueError("Number not a Fibonacci number!")
    return nextFib


# 3
someDict = {}

def counter_simple(fn):
    """This is a wrapper function around counter function

    Args:
        fn: some function we want to count

    Returns:
        function: inner function 
    """
    cnt = 0
    def inner(*args, **kwargs):
        """This function counts the number of times a function has been called. 

        Returns:
            fn:  function
        """
        global someDict
        nonlocal cnt
        cnt += 1
        print("{} has been called {} times.".format(fn.__name__, cnt))
        someDict[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

def add(a, b):
  return a+b

def mult(a, b):
  return a*b

def div(a, b):
  return a/b

# 4

someDict2 = {}
someDict3 = {}

def counter_specific(fn, dict2update):
    """This is a wrapper function around the counter function which updates specific dictionaries

    Args:
        fn (function): function we want to count
        dict2update (dict): dictionary we want to update

    Returns:
        function : inner function
    """
    cnt = 0

    def inner(*args, **kwargs):
        """This is a counter function which updates specific dictionaries

        Returns:
            dict: dict we want to update
        """
        nonlocal cnt
        cnt += 1
        print("{} has been called {} times.".format(fn.__name__, cnt))
        dict2update[fn.__name__] = cnt
        return dict2update
    return inner
