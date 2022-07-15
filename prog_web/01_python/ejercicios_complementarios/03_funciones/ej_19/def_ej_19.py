def simplify_fraction(num: int, denom: int):
    '''
    Returns a simplified fraction.
    Example (6/63) returns (2/21)
            (20/10) returns (2/1)
    Also returns a boolean. True if the fraction is already simplified
                            False otherwise.
    '''
    minor_ = min(num, denom)
    for i in range(minor_, 1, -1):
        if (num % i == 0) and (denom % i == 0):
            return int(num/i),int(denom/i), False
    return num, denom, True

def is_positive(a : int, b : int):
    '''
    returns True if a/b is positive
            False otherwise
    '''
    if a/b < 0:
        return False
    else:
        return True