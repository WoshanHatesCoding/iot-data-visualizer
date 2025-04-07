# 📡 IoT Device Simulator with Monitoring Dashboard

> 🧪 Simulate IoT sensor behavior, process live data, and visualize everything on a dynamic dashboard — all in Python.

---

## 📝 Description

This project is a Python-based simulator that mimics the behavior of a real IoT device. It includes:

- 🎛️ Sensor simulation  
- 🧠 Data analytics (min, max, average)  
- 📡 Communication emulation  
- 📊 Real-time dashboard  
- ✅ Unit testing  
- 🚫 Exception handling  
- 📦 Modular, clean code structure

It was developed as part of a programming assignment to practice Python skills such as **OOP**, **exception handling**, **standard libraries**, **modules**, and **visualization**.

---

## 🎯 Objectives

- Simulate a real-world sensor using a custom `Sensor` class  
- Perform basic analytics on incoming data with a `DataProcessor`  
- Transmit data using a `Communication` handler  
- Bundle all components into a `Device` class  
- Display analytics in real-time using a `Dashboard` (via `matplotlib`)  
- Write and run test cases using `unittest`  
- Organize all code using Python packages and modules  

---

## ⚙️ Project Structure

```
iot_device_simulator/
│
├── __init__.py
├── sensor.py              # Simulates sensor readings
├── data_processor.py      # Analyzes the sensor data
├── communication.py       # Handles communication layer
├── device.py              # Integrates sensor, processor, and comms
├── dashboard.py           # Displays data visually using matplotlib
├── main.py                # Runs the full simulation
└── tests/
    ├── __init__.py
    └── test_iot_device_simulator.py  # Unit tests
```

---

## 📈 Dashboard

- Displays real-time line graphs for:
  - Minimum value
  - Maximum value
  - Average value  
- Built with `matplotlib`  
- Auto-refreshes every iteration of data collection  

---

## 🚀 How to Run

### ▶️ Run the Simulation

1. Make sure you have Python 3 installed  
2. Install dependencies (only `matplotlib` is required):  
   ```bash
   pip install matplotlib
   ```
3. Run the simulation:  
   ```bash
   python main.py
   ```

> ⏸️ Press `Ctrl+C` to stop the simulation at any time.

---

## 🧪 Run Tests

This project uses Python’s built-in `unittest` framework.  
```bash
python -m unittest discover
```

---

## 💡 Extensions (Extra Credit Ideas)

- 🔄 Simulate multiple IoT devices  
- 🌡 Add new sensor types (e.g., temperature, humidity)  
- 🧮 Use advanced analytics (moving averages, filters)  
- 💾 Save data to a file or database  
- 📊 Upgrade dashboard using `plotly` or `dash`  

---

## 👨‍💻 Skills Practiced

- Object-Oriented Programming  
- Exception Handling  
- Modular Design  
- Data Visualization  
- Unit Testing  
- Python Standard Library  
