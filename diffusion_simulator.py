"""
Diffusion simulator for 2D Monte Carlo advection-diffusion processes.

This module defines the core function `diffusion_walk()` for simulating
particle-based PDE solutions with reflective boundaries and flexible diffusion models.
"""
import numpy as np
from geometry import find_intersection, find_reflection_angle
from vector_utils import rotate_vector_batched
from step_models import generate_step

EPS = 1e-10  # Small epsilon to prevent repeated intersection at the same wall

def diffusion_walk(
        X0,
        T0_vals,
        time_final,
        diff,
        iterations,
        walls,
        diffusion_model = "constant",
        seed = None
    ):
    """
    Simulates 2D Brownian motion with reflective boundaries using a Monte Carlo method.

    Particles follow stochastic paths with drift and diffusion, and are reflected upon
    intersecting user-defined wall boundaries. Suitable for modeling 2D advection-diffusion
    processes in bounded domains.

    Parameters
    ----------
    X0 : ndarray of shape (N, 2)
        Initial x and y positions for N particles.

    T0_vals : ndarray of shape (N,)
        Initial scalar weights or field values associated with each particle.
        These values are updated at each step of the simulation.

    final_time : float
        Total duration of the simulation.

    dt : float
        Time step for each iteration.

    diff : float
        Diffusion coefficient.

    iterations : int
        Number of time steps to simulate.

    walls : ndarray of shape (W, 2, 2)
        Array of wall line segments. Each wall is defined by two 2D points (P1, P2).

    diffusion_model: str, optional
        Type of diffusion model to use. Options are:
        - "constant": uses standard Brownian motion with fixed diffusion coefficient
        - "mapped": allows spatially varying or transformed diffusion steps
            (e.g., for mapped domains)

    seed : int, optional
        Random seed for reproducibility. If None (default), the random number generator
        is not explicitly seeded, and results will vary across runs.

    Returns
    -------
    X : ndarray of shape (N, iterations, 2)
        Particle positions at each time step for the entire simulation.
    """

    if seed is not None:
        np.random.seed(seed)
    
    N = X0.shape[0]  # Number of particles
    W = walls.shape[0]  # Number of walls
    dt = time_final/iterations  # Step size
    
    # Initialize particle position array
    # Shape: (num_particles, num_timesteps, 2 spatial dimensions)
    X = np.zeros((N, iterations, 2))
    X[:, 0, :] = X0 # Set initial positions

    # Initialize particle weight array
    # Shape: (num_particles, num_timesteps)
    T_vals = np.zeros((N, iterations))  # shape: (N, iterations)
    T_vals[:, 0] = T0_vals  # Set initial T values

    for i in range(1, iterations):

        # --- 1. Generate Proposed Step ---
        
        # Get current position for all particles 
        current_pos = X[:, i - 1, :]  # shape: (N, 2)

        # Generate Brownian motion step (constant or mapped diffusion)
        next_step = generate_step(
            current_pos,
            dt, 
            diff, 
            T_vals, 
            diffusion_model)

        # The next step will be checked for wall collisions below
        while True:
            
            # --- 2. Compute Wall Distances and Select the Closest Intersection ---

            # Compute tentative next position for all particles
            new_pos = current_pos + next_step  # shape: (N, 2)
        
            # Check for intersections between particle paths and wall segments
            # Returns wall_hit: (N, W, 2) and wall_intersected: (N, W) boolean
            wall_hit, wall_intersected = find_intersection(
                current_pos, 
                new_pos,
                walls[:, 0, :], 
                walls[:, 1, :]
            )
            
            # Compute distance to each intersected wall hit point
            wall_residuals = current_pos[:, None, :] - wall_hit  # shape: (N, W)
            wall_distances = np.linalg.norm(
                wall_residuals, 
                axis = -1
            )  # shape: (N, W)

            # Ignore walls that weren't actually intersected
            wall_distances[~wall_intersected] = np.inf

            # Select the closest intersected wall for each particle
            closest_wall_index = np.argmin(
                wall_distances, 
                axis=-1
            )  # shape: (N,)
            particle_range = np.arange(N)

            # --- 3. Exact Hit Points, Intersected Walls, and Compute Reflection Angles ---

            # Extract the actual hit position for the closest wall (per particle)
            closest_hit_pos = wall_hit[
                particle_range,
                closest_wall_index, 
                :
            ]  # shape: (N, 2)

            # Extract the wall geometry (two endpoints) for the closest wall
            closest_wall = walls[
                closest_wall_index,
                :,
                :
            ]  # shape: (N, 2, 2)

            # Determine which particles actually intersected a wall this step
            particle_intersected = wall_intersected[
                particle_range, 
                closest_wall_index
            ]  # shape: (N,)

            # Compute angle of reflection based on incidence direction and wall
            angle_of_reflection = find_reflection_angle(
                current_pos, 
                new_pos, 
                closest_wall
            )  # shape: (N,)

            # --- 4. Compute Reflection Vector ---

            # Compute full step vector before wall intersection
            step_vector = new_pos - current_pos  # shape: (N, 2)

            # Rotate the vector to reflect off the wall surface
            v_rotated = rotate_vector_batched(
                angle_of_reflection,
                step_vector
            )  # shape: (N,2)

            # Determine remaining distance after hitting the wall
            total_step_len = np.linalg.norm(
                step_vector,
                axis = -1
            )  # shape: (N,)
            remaining_step_len = np.linalg.norm(
                closest_hit_pos - new_pos,
                axis = -1
            )  # shape: (N,)

            # Avoid division by zero
            scale_factor = remaining_step_len / (total_step_len + EPS)

            # Scale rotated vector to preserve total step length
            v_rotated = v_rotated * scale_factor[:, None]  # shape: (N, 2)

            # --- 5. Handle Wall Bounce vs no Bounce ---

            # For intersected particles: move to wall and step slightly back from it
            current_pos_bounce = \
                closest_hit_pos - EPS * (closest_hit_pos - current_pos)

            # For non-intersected: use proposed new
            current_pos_nobounce = new_pos

            # Select final position based on intersection
            current_pos = np.where(
                particle_intersected[:, None],
                current_pos_bounce,
                current_pos_nobounce
            )

            # Prepare next step: rotated vector if bounced, zero otherwise
            next_step_bounce = v_rotated
            next_step_nobounce = np.zeros((N, 2))
            next_step = np.where(
                particle_intersected[:, None],
                next_step_bounce,
                next_step_nobounce
            )

            # If no particles intersected any walls, exit the loop
            if np.all(~particle_intersected):
                break

        # --- 6. Store Final Position After Wall Reflection ---

        # Once all reflections are resolved, store the updated particle positions
        X[:, i, :] = current_pos

    return X  # shape: (N, iterations, 2) - final particle positions over time