import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import glob

from sympy.physics.control.control_plots import matplotlib

matplotlib.use('Qt5Agg')

csv_file = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_sensors/P2"

csv_files = glob.glob(csv_file + "/*.csv")
dfs = []
counter = 0
for filename in sorted(csv_files):
    #if counter > 1:
    #    break
    df = pd.read_csv(filename)
    dfs.append(df)
    counter += 1
combined_df = pd.concat(dfs, ignore_index=True)

print(combined_df)

fig, axs = plt.subplots(2, figsize=(10, 10))
axs[0].plot(combined_df["timestamp"], combined_df["Ch1"], color="blue")
axs[0].xaxis.set_major_locator(MaxNLocator(nbins=3))
axs[1].plot(combined_df["timestamp"], combined_df["Ch2"], color="red")
axs[1].xaxis.set_major_locator(MaxNLocator(nbins=3))

plt.show()
