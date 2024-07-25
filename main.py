import sys
import os

# Add the current directory to the Python path
sys.path.append(os.getcwd())

from grid_manager import GridManager
from math_functions import all_functions
from grid_initializers import normal_distribution, positional_values, random_values

# Create a GridManager instance
grid_manager = GridManager(grid_size=(100, 100))

# Add grids with different initialization techniques
grid_manager.add_grid(normal_distribution, "Normal Distribution")
grid_manager.add_grid(positional_values, "Positional Values")
grid_manager.add_grid(random_values, "Random Values")

# Process and plot all grids
grid_manager.process_and_plot_all_grids(all_functions)

grid_manager.process_and_plot_all_grids_together()