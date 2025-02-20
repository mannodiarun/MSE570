import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

# Path to LAMMPS log file
log_file_path = "log.lammps"

# Read the LAMMPS log file
with open(log_file_path, "r") as file:
    log_lines = file.readlines()

# Extract Step and Temperature data
step_temp_data = []
capture = False

for line in log_lines:
    if re.match(r"^\s*Step\s+Temp", line):  # Find header
        capture = True
        continue
    if capture and re.match(r"^\s*\d+", line):  # Capture numerical data
        parts = line.split()
        step = int(parts[0])  # Step
        temp = float(parts[1])  # Temperature
        step_temp_data.append((step, temp))
    elif capture and not line.strip():  # Stop if empty line
        break

# Convert to DataFrame
df = pd.DataFrame(step_temp_data, columns=["Step", "Temperature"])

# Convert Step to Time (Time in ps)
timestep_ps = 0.001  # 1 fs = 0.001 ps
df["Time (ps)"] = df["Step"] * timestep_ps

# Plot Time vs Temperature
plt.figure(figsize=(8, 5))
plt.plot(df["Time (ps)"], df["Temperature"], marker="o", linestyle="-", markersize=3, label="Temperature")

plt.xlabel("Time (ps)")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs Time in LAMMPS Simulation")
plt.legend()
plt.grid(True)
plt.show()

# Extract Temperature and Potential Energy (PotEng) data
step_pe_data = []
capture = False

for line in log_lines:
    if re.match(r"^\s*Step\s+Temp\s+PotEng", line):  # Find header
        capture = True
        continue
    if capture and re.match(r"^\s*\d+", line):  # Capture numerical data
        parts = line.split()
        temp = float(parts[1])  # Temperature
        pe = float(parts[2])  # Potential Energy
        step_pe_data.append((temp, pe))
    elif capture and not line.strip():  # Stop if empty line
        break

# Convert to DataFrame
df_pe = pd.DataFrame(step_pe_data, columns=["Temperature", "Potential Energy"])

# Plot Temperature vs Potential Energy
plt.figure(figsize=(8, 5))
plt.plot(df_pe["Temperature"], df_pe["Potential Energy"], marker="o", linestyle="-", markersize=3)

plt.xlabel("Temperature (K)")
plt.ylabel("Potential Energy (eV)")
#plt.title("Potential Energy vs Temperature in LAMMPS Simulation")
plt.grid(True)
plt.show()
