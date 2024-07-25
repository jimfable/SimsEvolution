import numpy as np
import matplotlib.pyplot as plt
from math_functions import divide, modulus, simple_functions, complex_functions, all_functions
from grid_initializers import grid_initializers

class GridManager:
    def __init__(self, grid_size=(100, 100)):
        self.grid_size = grid_size
        self.grids = []
        self.titles = []
        self.processed_grids = []  # New attribute to store processed grids

    def add_grid(self, init_function, title):
        grid = np.zeros(self.grid_size, dtype=object)
        init_function(grid)
        self.grids.append(grid)
        self.titles.append(title)

    def process_grid(self, grid, functions):
        Z = np.zeros(self.grid_size)

        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                func = np.random.choice(functions)
                x, y = float(grid[i, j][0]), float(grid[i, j][1])
                if func in [divide, modulus] and y == 0:
                    y = 1  # Avoid zero for division and modulus
                try:
                    result = func(x, y)
                    if isinstance(result, complex):
                        result = result.real  # Convert complex result to its real part
                    Z[i, j] = result
                except Exception as e:
                    Z[i, j] = 0  # Handle any unexpected errors

        # Normalize the results using a logarithmic scale
        Z = np.log1p(np.abs(Z))  # Apply log(1 + |Z|) to handle negative values and compress the range
        Z = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))  # Normalize to range [0, 1]
        Z = np.round(Z, 2)

        return Z

    def plot_grid(self, Z, title):
        # Use a different colormap and adjust color limits
        plt.imshow(Z, cmap='plasma', vmin=0, vmax=1)
        plt.colorbar()
        plt.title(title)
        plt.show()

    def process_and_plot_grid(self, grid, title, functions):
        Z = self.process_grid(grid, functions)
        self.processed_grids.append((Z, title))
        self.plot_grid(Z, title)

    def process_all_grids(self, functions):
        self.processed_grids = []
        for grid, title in zip(self.grids, self.titles):
            Z = self.process_grid(grid, functions)
            self.processed_grids.append((Z, title))

    def plot_all_grids(self):
        for Z, title in self.processed_grids:
            self.plot_grid(Z, title)

    def process_and_plot_all_grids(self, functions):
        self.process_all_grids(functions)
        self.plot_all_grids()

    def plot_all_grids_together(self):
        num_grids = len(self.processed_grids)
        fig, axes = plt.subplots(1, num_grids, figsize=(15, 5))  # Adjust the figsize as needed

        for ax, (Z, title) in zip(axes, self.processed_grids):
            # Use a different colormap and adjust color limits
            im = ax.imshow(Z, cmap='plasma', vmin=0, vmax=1)
            ax.set_title(title)
            fig.colorbar(im, ax=ax)

        plt.tight_layout()
        plt.show()