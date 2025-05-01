'''
I/O utilities for saving simulation results.

This module provides helper functions for exporting simulation data
to disk in binary (.npz), text (.csv), and config (.json) formats.

Intended for use with 1D/2D Monte Carlo simulation frameworks.
'''
import numpy as np
import json

def save_simulation_data(X, filename_prefix="simulation_output"):
    """
    Saves simulation output array X to disk in both .npz and .csv formats.

    Parameters
    ----------
    X : ndarray of shape (N, T, 2)
        The simulation output, where:
        - N = number of particles
        - T = number of timesteps
        - 2 = spatial dimensions (x, y)

    filename_prefix : str
        Base name to use for the saved files. This function appends
        `.npz` and `.csv` extensions automatically.

    Outputs
    -------
    - <filename_prefix>.npz : NumPy binary file containing the full array
    - <filename_prefix>.csv : Flattened CSV file with columns: particle, time, x, y
    """

    np.savez(f"{filename_prefix}.npz", X=X)

    N, T, D = X.shape
    X_flat = X.reshape(N * T, D)
    particle_ids = np.repeat(np.arange(N), T)
    time_steps = np.tile(np.arange(T), N)
    csv_data = np.column_stack((particle_ids, time_steps, X_flat))

    np.savetxt(
        f"{filename_prefix}.csv",
        csv_data,
        delimiter=",",
        header="particle,time,x,y",
        comments=''
    )


def save_config_to_json(config, filename_prefix="simulation_output"):
    """
    Saves the simulation configuration dictionary to a JSON file.

    Parameters
    ----------
    config : dict
        Dictionary of simulation parameters and metadata.

    filename_prefix : str
        Base name for the output file. Adds `.json` automatically.
    """
    with open(f"{filename_prefix}_config.json", "w") as f:
        json.dump(config, f, indent=4)
