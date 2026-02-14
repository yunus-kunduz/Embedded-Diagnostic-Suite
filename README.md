# Embedded Diagnostic Suite & HIL Simulator

This project is designed to perform Hardware-in-the-Loop (HIL) simulation via Python without requiring a physical STM32 board.

## 🚀 Features

* **Virtual MCU Emulator:** Generates noisy sensor data through a COM port.

* **Digital Signal Processing (DSP):** Applies a real-time Low Pass Filter.

* **Live Visualization:** Displays raw and filtered data in real-time graphs using Matplotlib.

## 📊 Mathematical Model

The filter equation used:

$$y[n] = \alpha \cdot x[n] + (1 - \alpha) \cdot y[n-1]$$

## 🛠 Installation

1. Set up a COM1–COM2 bridge using VSPE.

2. pip install -r requirements.txt

3. Run mcu_emulator.py first, then run diagnostic_suite.py.
