# Quantum Random Number Generator 🎲⚛️

This project is a **Quantum Random Number Generator (QRNG)** implemented in Python using [Cirq](https://github.com/quantumlib/Cirq), a quantum computing framework by Google. It generates truly random numbers by leveraging quantum superposition and measurement.

## 🔍 What It Does

The script uses a 4-qubit quantum circuit to generate a random 4-bit binary number. This binary string is then mapped to a decimal number between 0 and 9. By repeating this process multiple times, the program creates a multi-digit random number with quantum-level randomness.

## 📦 Requirements

- Python 3.7+
- [Cirq](https://pypi.org/project/cirq/)
- NumPy

### Installation

```bash
pip install cirq numpy
