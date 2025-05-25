# 2D PDE Simulation Framework 🚀

![GitHub Repo stars](https://img.shields.io/github/stars/braxten626/2d-pde-simulation-framework?style=social) ![GitHub forks](https://img.shields.io/github/forks/braxten626/2d-pde-simulation-framework?style=social) ![GitHub issues](https://img.shields.io/github/issues/braxten626/2d-pde-simulation-framework) ![GitHub license](https://img.shields.io/github/license/braxten626/2d-pde-simulation-framework)

## Overview

Welcome to the **2D PDE Simulation Framework**! This project provides a Monte Carlo framework designed for 2D divergence-dependent partial differential equations (PDEs). It includes features for coordinate mapping and supports general polygonal domains. 

You can find the latest releases of the framework [here](https://github.com/braxten626/2d-pde-simulation-framework/releases). Download the files and execute them to start your simulation.

## Table of Contents

- [Features](#features)
- [Topics](#topics)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Monte Carlo Simulations**: Utilize probabilistic methods for solving complex PDEs.
- **Divergence-Dependent PDEs**: Specifically designed for equations that depend on divergence, making it suitable for a variety of applications.
- **Coordinate Mapping**: Transform coordinates easily for better simulations in different geometries.
- **Polygonal Domains**: Handle general polygonal shapes, providing flexibility in modeling real-world problems.
- **Interoperability**: Written in Fortran with Python bindings for ease of use.

## Topics

This repository covers a range of topics relevant to computational mathematics and scientific computing:

- Advection-Diffusion
- Computational Geometry
- Divergence Drift
- Fortran
- Numerical Simulation
- Partial Differential Equations (PDE)
- Polygonal Domains
- Probabilistic Programming
- Python
- Research Code
- Scientific Computing

## Installation

To get started with the **2D PDE Simulation Framework**, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/braxten626/2d-pde-simulation-framework.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd 2d-pde-simulation-framework
   ```

3. **Install Dependencies**:
   Make sure you have Fortran and Python installed. You can install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Compile the Fortran Code**:
   Use the following command to compile the Fortran code:
   ```bash
   make
   ```

5. **Run the Simulation**:
   After compilation, you can run the simulation using:
   ```bash
   python run_simulation.py
   ```

## Usage

The framework is designed for ease of use. Once installed, you can set up your simulation parameters in the configuration file. Here's a basic example:

```json
{
  "domain": "polygon",
  "shape": [[0,0], [1,0], [1,1], [0,1]],
  "initial_conditions": "sin(pi*x)*sin(pi*y)",
  "time_steps": 1000,
  "output": "results.txt"
}
```

### Running the Simulation

To execute the simulation, use the following command:

```bash
python run_simulation.py --config config.json
```

### Output

The results will be saved in the specified output file. You can visualize the results using any data visualization tool of your choice.

## Examples

Here are some examples of how to set up different simulations:

### Example 1: Simple Square Domain

```json
{
  "domain": "square",
  "shape": [[0,0], [1,0], [1,1], [0,1]],
  "initial_conditions": "1.0",
  "time_steps": 500,
  "output": "square_results.txt"
}
```

### Example 2: Complex Polygonal Domain

```json
{
  "domain": "polygon",
  "shape": [[0,0], [2,0], [2,1], [1,2], [0,1]],
  "initial_conditions": "exp(-((x-1)^2 + (y-1)^2))",
  "time_steps": 1000,
  "output": "polygon_results.txt"
}
```

## Contributing

We welcome contributions to the **2D PDE Simulation Framework**! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, feel free to reach out:

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [braxten626](https://github.com/braxten626)

You can find the latest releases of the framework [here](https://github.com/braxten626/2d-pde-simulation-framework/releases). Download the files and execute them to start your simulation.

Thank you for checking out the **2D PDE Simulation Framework**! We hope you find it useful for your research and projects.