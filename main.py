"""
Main script to run the Monte Carlo simulation for 2D divergence-dependent PDEs 
with coordinate mapping and general polygonal domains.

This script pulls parameters from the parameters module and executes the
advection_diffusion function, which approximates the solution to a stochastic
PDE using a particle-based Monte Carlo method.
"""

from Simulate_Brownain_Motion import advection_diffusion_walk
from Parameters import parameters


def main():
    seed = parameters["seed"]
    number_of_steps = parameters["number_of_steps"]
    number_of_realizations = parameters["number_of_realizations"]
    final_time = parameters["final_time"]
    diffusion_coefficient = parameters["diffusion_coefficient"]
    initial_positions = parameters["initial_positions"]
    initial_T_values = parameters["initial_T_values"]

    advection_diffusion_walk(
        number_of_steps,
        number_of_realizations,
        diffusion_coefficient,
        final_time / number_of_steps,
        initial_positions,
        initial_T_values,
        seed
    )

if __name__ == "__main__":
    main()
