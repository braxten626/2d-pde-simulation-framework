"""
Configuration file for runtime parameters used in the Monte Carlo solver.

Includes settings for simulation duration, particle count, and initialization.
"""

import numpy as np

number_of_realizations = 10**6

config = {
    "seed": 52,
    "number_of_steps": 10**4,
    "number_of_realizations": number_of_realizations,
    "final_time": 1.0,
    "diffusion_coefficient": 1.0,
    "number_of_bins_in_histogram": 100,
}

# Initialize input arrays
config["initial_positions"] = np.zeros(number_of_realizations)
config["initial_T_values"] = np.ones(number_of_realizations)
