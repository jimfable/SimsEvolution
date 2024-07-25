import numpy as np

# Define mathematical functions
def add(x, y):
    result = x + y
    return result.real if isinstance(result, complex) else result

def subtract(x, y):
    result = x - y
    return result.real if isinstance(result, complex) else result

def multiply(x, y):
    result = x * y
    return result.real if isinstance(result, complex) else result

def divide(x, y):
    if y != 0:
        result = x / y
        return result.real if isinstance(result, complex) else result
    else:
        return 0

def power(x, y):
    try:
        # Limit the range of x and y to avoid overflow
        if abs(x) > 10 or abs(y) > 10:
            return 0
        result = x ** y
        return result.real if isinstance(result, complex) else result
    except (ValueError, OverflowError):
        return 0  # Return 0 if the power operation is invalid or causes overflow

def modulus(x, y):
    if y != 0:
        result = x % y
        return result.real if isinstance(result, complex) else result
    else:
        return 0

def sine(x, y):
    result = np.sin(x) + np.sin(y)
    return result.real if isinstance(result, complex) else result

def cosine(x, y):
    result = np.cos(x) + np.cos(y)
    return result.real if isinstance(result, complex) else result

def exponential(x, y):
    try:
        result = np.exp(x) + np.exp(y)
        return result.real if isinstance(result, complex) else result
    except OverflowError:
        return 0  # Return 0 if the exponential operation causes overflow

def tanh(x, y):
    result = np.tanh(x) + np.tanh(y)
    return result.real if isinstance(result, complex) else result

def log(x, y):
    try:
        result = np.log1p(np.abs(x)) + np.log1p(np.abs(y))
        return result.real if isinstance(result, complex) else result
    except ValueError:
        return 0  # Return 0 if log operation is invalid

# Lists of functions
simple_functions = [add, subtract, multiply, divide, modulus]
complex_functions = [power, sine, cosine, exponential, tanh, log]
all_functions = simple_functions + complex_functions