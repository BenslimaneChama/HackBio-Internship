import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from stage1library import generate_growth_curves
from stage1library import find_80_percent_density

# Inputs
unit_type = input("Time unit (h, min, s): ").strip().lower()
time_period = int(input("Time period: ")) * (60 if unit_type == 'h' else 1)
per_unit_record = int(input(f"Points per {unit_type}: "))
col_numbers = time_period * per_unit_record
raw_numbers = int(input("Number of graphs: "))
starting_point = float(input("Starting density (or 0 for random): ")) or round(random.uniform(1.0, 100.0), 2)

use_expo_range = input("Do you want to define the exponential phase range? (y/n): ").strip().lower()
expo_start, expo_end = (None, None)
if use_expo_range == 'y':
    expo_start = int(input("Enter start of exponential phase: "))
    expo_end = int(input("Enter end of exponential phase: "))

data = generate_growth_curves(unit_type, time_period, col_numbers, raw_numbers, starting_point, expo_start, expo_end)
max_density, time_80, density_80 = find_80_percent_density(data, time_step=1)
print(f"Max Density : {max_density}, Areaches 80% at {time_80} {unit_type}, with a density = {density_80}")