"""
Configuration module for 2D Monte Carlo advection-diffusion simulations.

This module provides a centralized interface for defining simulation parameters,
initial conditions, and domain-specific geometry. It returns a fully constructed
dictionary containing all values needed to run a simulation.

Supports optional overrides for flexibility and future integration with YAML/JSON configs.
"""
import numpy as np
from geometry import define_wall_segments

def load_config(overrides=None):
    """
    Initializes and returns a general-purpose simulation configuration dictionary.

    Parameters
    ----------
    overrides : dict, optional
        A dictionary of values to override default settings.

    Returns
    -------
    config : dict
        Fully constructed configuration dictionary with derived arrays.
    """

    # 1. Base default configuration
    config = {
        "seed": 52,
        "number_of_realizations": 10**6,
        "final_time": 1.0,
        "diffusion_coefficient": 1.0,
        "number_of_bins_in_histogram": 100,
        "domain_type": "half_plane",
        "domain_size": 1.0,
        "diffusion_model": "constant",
    }

    # 2. Apply user overrides if provided
    if overrides:
        config.update(overrides)

    # 3. Derived arrays
    config["initial_positions"] = np.zeros(config["number_of_realizations"])
    config["initial_T_values"] = np.ones(config["number_of_realizations"])
    config["wall_array"] = define_wall_segments(
        config["domain_type"],
        config["domain_size"]
    )

    return config
