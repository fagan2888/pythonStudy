s = '0'
n = int(s)
print('n = %d' % n)

def abs(n):
    '''
    Function to get absolute value of number.
    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

print(abs(0))