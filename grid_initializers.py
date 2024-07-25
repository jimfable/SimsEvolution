import numpy as np

def normal_distribution(grid, mean=0, std=200):
    grid_size = grid.shape
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            x = np.random.normal(mean, std)
            y = np.random.normal(mean, std)
            grid[i, j] = (f'{x}', f'{y}')

def positional_values(grid, scale_range=(0.5, 1.5)):
    grid_size = grid.shape
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            x = i * np.random.uniform(*scale_range)
            y = j * np.random.uniform(*scale_range)
            grid[i, j] = (f'{x}', f'{y}')

def random_values(grid, value_range=(-200, 200)):
    grid_size = grid.shape
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            x = np.random.uniform(*value_range)
            y = np.random.uniform(*value_range)
            grid[i, j] = (f'{x}', f'{y}')

def normalized_positional_values(grid):
    grid_size = grid.shape
    max_x, max_y = grid_size[0] - 1, grid_size[1] - 1
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            x = i / max_x
            y = j / max_y
            grid[i, j] = (f'{x}', f'{y}')



grid_initializers = [normal_distribution, positional_values, random_values, normalized_positional_values]
grid_initializers = [normal_distribution, positional_values, random_values, normalized_positional_values]
