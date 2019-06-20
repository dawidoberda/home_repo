def add(x,y):
    """Add Function"""
    return x + y


def substract(x, y):
    """Substracting function"""
    return x-y


def multiply(x, y):
    """Multypling function"""
    return x * y


def divide(x, y):
    """Divide function"""
    if y == 0 :
        raise ValueError('Cannot divide by zero')
    return x / y