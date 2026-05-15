"""
generate_data.py
----------------
Synthetic data generation for the Pulse Rate Case Study.

Generates a dataset of 25 adult subjects with realistic physiological
measurements using numpy.random. The output CSV is used as input for
the SAS Studio statistical analysis pipeline.

Author: Chiemela Joseph Nwosu
"""

import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

N = 25  # number of subjects

# Generate each variable within realistic physiological ranges
age     = np.random.randint(20, 65, N)
weight  = np.round(np.random.uniform(50.0, 100.0, N), 4)   # kg
height  = np.round(np.random.uniform(150.0, 200.0, N), 4)  # cm
gender  = np.random.randint(0, 2, N)                        # 0 = Female, 1 = Male
wbc     = np.round(np.random.uniform(4.0, 11.0, N), 4)     # x10^9/L
rbc     = np.round(np.random.uniform(4.5, 6.0, N), 4)      # x10^12/L
pulse   = np.round(np.random.uniform(27.0, 67.0, N), 4)    # bpm (resting)

data = pd.DataFrame({
    "Age":    age,
    "Weight": weight,
    "Height": height,
    "Gender": gender,
    "WBC":    wbc,
    "RBC":    rbc,
    "Pulse":  pulse,
})

# Export to CSV for use in SAS Studio
output_path = "pulse_rate_data.csv"
data.to_csv(output_path, index=False)

print(f"Dataset generated: {N} subjects, {data.shape[1]} variables")
print(f"Saved to: {output_path}\n")
print(data.to_string(index=False))
