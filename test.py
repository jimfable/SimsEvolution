import numpy as np
import matplotlib.pyplot as plt

# Define more complex functions
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

functions = [add, subtract, multiply, divide, power, modulus, sine, cosine, exponential]

function1 = [add, subtract, multiply, divide]


# Increase the range of random values and use normal distribution
small_grid = np.zeros((1000, 1000), dtype=object)

for i in range(small_grid.shape[0]):
    for j in range(small_grid.shape[1]):
        x = np.random.normal(0, 100)  # Normal distribution with mean 0 and std 100
        y = np.random.normal(0, 100)  # Normal distribution with mean 0 and std 100
        small_grid[i, j] = (f'{x}', f'{y}')

#print(small_grid)

# ... existing code ...

Z = np.zeros((1000, 1000))

for i in range(small_grid.shape[0]):
    for j in range(small_grid.shape[1]):
        func = np.random.choice(list(function1))
        x, y = float(small_grid[i, j][0]), float(small_grid[i, j][1])
        if func in [divide, modulus] and y == 0:
            y = 1  # Avoid zero for division and modulus
        try:
            result = func(x, y)
            if isinstance(result, complex):
                result = result.real  # Convert complex result to its real part
            Z[i, j] = result
            #if i < 5 and j < 5:  # Print values for the first few elements
            #    print(f"Z[{i}, {j}] = {result} (x={x}, y={y}, func={func.__name__})")
        except Exception as e:
            Z[i, j] = 0  # Handle any unexpected errors

# Print some statistics about Z
print(f"Z min: {np.min(Z)}, Z max: {np.max(Z)}, Z mean: {np.mean(Z)}, Z std: {np.std(Z)}")

# Normalize the results using a logarithmic scale
Z = np.log1p(np.abs(Z))  # Apply log(1 + |Z|) to handle negative values and compress the range
Z = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))  # Normalize to range [0, 1]
Z = np.round(Z, 2)

print("Generated Z grid:")
print(Z)
#print(f"Minimum value in Z: {np.min(Z)}")
#print(f"Maximum value in Z: {np.max(Z)}")

# Use a different colormap and adjust color limits
plt.imshow(Z, cmap='plasma', vmin=0, vmax=1)
plt.colorbar()
plt.show()

