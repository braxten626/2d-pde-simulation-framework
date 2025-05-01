# Probabilistic Simulation Framework for 2D PDEs

This repository presents a representative simulation framework for solving divergence-dependent partial differential equations (PDEs) using Monte Carlo methods. It models stochastic particle behavior in two-dimensional domains with reflecting boundary conditions and compares results to known analytical solutions.

> ⚠️ This public repository reflects the structure and capabilities of a broader research codebase developed as part of my graduate work at UNC Chapel Hill. Core implementation details and sensitive methods have been omitted or replaced with pseudocode for confidentiality.

---

## 🔍 Project Overview

- Models 2D advection-diffusion equations with divergence-dependent drift
- Supports boundary reflections in complex geometries (e.g., half-plane, quarter-plane, L-shaped domain)
- Leverages probabilistic sampling to approximate PDE solutions
- Includes statistical tools for comparing simulation output with exact solutions
- Incorporates coordinate mappings to simplify PDE structure in transformed domains

---

## 🧱 Project Structure

```text
📁 2D_results/                          # Output folder for CSVs and figures
│   ├── fort.1                          # Simulation output file (Tu, Tv, Q fields)
│   ├── Exact_v_Sim.png                 # Heatmap of simulation vs. exact solution
│   └── Exact_v_Map.png                 # Solution comparison in mapped coordinates

📁 2D_Brownian_Motion_N_Walls/
│   ├── Main.py                            # Entry point: orchestrates full simulation workflow
│   ├── Parameters.py                      # Defines simulation parameters (domain, time, drift, diffusion, etc.)
│   ├── Simulate_Brownain_Motion.py        # Simulates 2D Brownian motion with drift and boundary reflection
│   └── Compute_Geometry_Calculations.py   # Computes wall normals, intersections, and reflection angles

📄 README.md                            # Project overview (you're here!)

'''text

---

## 🔒 Access & License

This repository is for **demonstration purposes only**. Some files and methods have been withheld for confidentiality.  
Please do not reuse or redistribute without written permission.

---

📬 **Contact:**  
If you'd like to learn more or discuss the project in a technical interview, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/madeline-preston) or [email](mailto:maddiepr@email.unc.edu).
