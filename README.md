# 🧪 Probabilistic Simulation Framework for 2D PDEs

This project implements a Monte Carlo simulation framework for solving divergence-dependent partial differential equations (PDEs) in 2D domains. It models stochastic particle dynamics with reflecting boundary conditions and supports coordinate mapping for solving PDEs in simplified geometries.

> 🚧 This repository is a **public-facing subset** of a larger research codebase developed as part of graduate work at UNC Chapel Hill. Some core components have been omitted or abstracted for confidentiality.

---

## 📁 Project Structure

```text
project_root/
├── config.py                   # Defines simulation parameters, initial conditions, and domain setup
├── diffusion_simulator.py      # Core simulation function for 2D advection-diffusion processes
├── geometry.py                 #
├── ititial_conditions.py       # 
├── main.py                     # Entry point for running a simulation using the config and simulator
├── utils/
│   ├── io.py                   # Functions to save simulation data (.csv, .npz) and configs (.json)
│   └── __init__.py             # Marks the utils folder as a package
├── step_models.py              #
├── vector_utils.py             # 
├── results/                    # Directory where simulation outputs are saved
└── README.md                   # Project overview, instructions, and documentation
```

---

## 📈 Features

- Simulates 2D advection-diffusion PDEs with divergence-dependent drift
- Supports reflecting walls and arbitrary polygonal geometries
- Allows custom coordinate mappings (e.g., half-plane, quarter-plane, L-shaped)
- Modular structure: plug in different step models and reflection rules
- Outputs `.npz`, `.csv`, and `.json` formats for easy analysis and reproducibility

---

## 🧪 Example Usage

Run the simulation from the terminal:

```bash
python Main.py
```
---

## 🔒 Access & License

This repository is for **demonstration purposes only**. Some files and methods have been withheld for confidentiality.  
Please do not reuse or redistribute without written permission.

---

📬 **Contact:**  
If you'd like to learn more or discuss the project in a technical interview, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/madeline-preston) or [email](mailto:maddiepr@email.unc.edu).
