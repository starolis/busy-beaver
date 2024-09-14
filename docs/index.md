# Busy Beaver Turing Machine Simulator

![License](https://img.shields.io/github/license/starolis/busy-beaver)
![Build Status](https://img.shields.io/github/actions/workflow/status/starolis/busy-beaver/python-app.yml?branch=main)
![Python Version](https://img.shields.io/badge/python-3.8%2C%203.9%2C%203.10-blue)

Welcome to the **Busy Beaver Turing Machine Simulator**! 🎉

## 🧠 What is a Busy Beaver? Does anyone know? Maybe?

The **Busy Beaver** problem explores the limits of computation by seeking the Turing machine with the maximum number of `1`s printed on the tape before halting, given a fixed number of states and symbols. It's a fascinating journey into the boundaries of what machines can compute.

## 🚀 Features

- **Modular Design:** Clean separation of concerns for scalability and maintainability.
- **Multiprocessing:** Efficiently simulates multiple Turing machines in parallel, speeding up the exploration process.
- **Comprehensive Reporting:** Identifies and reports the most productive and longest-running halting machines.
- **Extensible:** Easily modify the number of states, symbols, and other configurations to explore various scenarios.
- **User-Friendly Interface:** Simple scripts to run simulations and analyze results without diving deep into the codebase.

## 📚 Documentation

Explore the comprehensive documentation to get the most out of the simulator:

- [**Architecture Overview**](architecture.md): Dive into the system's design and understand how different components interact.
- [**Usage Guide**](usage.md): Step-by-step instructions on setting up and running simulations.
- [**Contributing**](../CONTRIBUTING.md): Want to contribute? Learn how you can help improve the simulator.
- [**API Reference**](api.md): Detailed information about the simulator's classes and functions.

## 🛠 Getting Started

Ready to explore the Busy Beaver problem? Here's how to get started:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/starolis/busy-beaver.git
   cd busy-beaver
   ```

2. **Set Up the Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Simulator**

    ```bash
    python run_simulation.py
    ```

## 🤝 Contributing

We welcome contributions to make this simulator even better! Check out our [Contributing Guidelines](../CONTRIBUTING.md) for more details.

## 📈 Results

After running simulations, you'll receive detailed reports highlighting:

- **Most Productive Machines:** Turing machines that print the highest number of 1s before halting.
- **Longest-Running Machines:** Machines that take the most steps to reach a halting state.

Explore these results to gain insights into the computational power and efficiency of different Turing machine configurations.

## 📄 License

This project is licensed under the MIT License.

## 📫 Contact

Have questions or feedback? Reach out to [matt@starol.is](mailto:matt@starol.is)

## 🎓 Acknowledgments

- Inspired by the fascinating concepts in Computation Theory.
- Powered by [MkDocs](https://www.mkdocs.org/) for seamless documentation.
