# Busy Beaver Turing Machine Simulator

A Python-based simulator to explore Busy Beaver Turing machines. This project enumerates all possible Turing machines with a given number of states and symbols, simulates each one, and identifies machines that produce the maximum number of `1`s on the tape or take the longest to halt.

## Features

- **Modular Design**: Clean separation of concerns for scalability.
- **Multiprocessing**: Efficiently simulates multiple Turing machines in parallel.
- **Comprehensive Reporting**: Identifies and reports the most productive and longest-running halting machines.
- **Extensible**: Easily modify the number of states, symbols, and other configurations.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/busy-beaver.git
   cd busy-beaver

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the simulation script:

```bash
python scripts/run_simulation.py
```

## Project Structure

```markdown
busy-beaver/
├── README.md
├── .gitignore
├── LICENSE
├── requirements.txt
├── setup.py
├── busy_beaver/
│   ├── __init__.py
│   ├── turing_machine.py
│   ├── simulation.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_turing_machine.py
│   └── test_simulation.py
├── scripts/
│   └── run_simulation.py
└── docs/
    └── architecture.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
