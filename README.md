# Embedded Diagnostic Suite & HIL Simulator

This project is a Python-based **Hardware-in-the-Loop (HIL)** simulation environment designed to develop and test embedded signal processing algorithms without requiring physical hardware like STM32.

## 🚀 Features
* **Virtual MCU Emulator:** Generates noisy sensor data (simulating 12-bit ADC) and transmits it over a virtual serial port (COM1).
* **Digital Signal Processing (DSP):** Implements a real-time **Low Pass Filter (LPF)** to eliminate high-frequency noise and stabilize sensor readings.
* **Live Visualization:** Features a dynamic **Matplotlib** dashboard for synchronized plotting of raw and filtered signals.
* **Serial Bridge Integration:** Leverages virtual null-modem cables (VSPE) for seamless inter-process communication.

## 📊 Mathematical Model
The signal processing core utilizes a Discrete-Time First-Order Low Pass Filter:

$$y[n] = \alpha \cdot x[n] + (1 - \alpha) \cdot y[n-1]$$

Where:
* $x[n]$ is the raw noisy input from the emulator.
* $y[n]$ is the pufified output.
* $\alpha$ is the smoothing factor (Alpha) used to balance latency and noise rejection.

## 🛠 Setup & Installation
1. **Virtual Ports:** Configure a virtual pair (e.g., COM1 <=> COM2) using VSPE.
2. **Dependencies:** Ensure you have the required libraries installed:
   ```bash
   pip install pyserial numpy matplotlib
