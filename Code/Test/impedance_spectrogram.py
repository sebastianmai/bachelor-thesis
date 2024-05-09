import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

csv_file = "/home/basti/measurements (47285)/ACM0_2024-05-08_15:51:42.csv"

df = pd.read_csv(csv_file, usecols=["datetime", "VVmax_CH1", "VImax_CH1"])
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S:%f')

fig, axs = plt.subplots(2, figsize=(10, 10))

# Plot VV_max_ch1
axs[0].plot(df["datetime"], df["VVmax_CH1"], color="blue")
axs[0].xaxis.set_major_locator(MaxNLocator(nbins=4))
axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
axs[0].set_xlabel("Time")
axs[0].set_ylabel("VV_max_ch1")
axs[0].set_title("VV_max_ch1 over time")

# Plot VImax_ch1
axs[1].plot(df["datetime"], df["VImax_CH1"], color="blue")
axs[1].xaxis.set_major_locator(MaxNLocator(nbins=4))
axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
axs[1].set_xlabel("Time")
axs[1].set_ylabel("VImax_ch1")
axs[1].set_title("VImax_ch1 over time")

plt.tight_layout()
plt.show()


df = pd.read_csv(csv_file, usecols=["datetime", "RMS_CH1"])
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S:%f')

plt.figure(figsize=(10, 5))
plt.plot(df["datetime"], df["RMS_CH1"], color="blue")

ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(nbins=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

plt.xlabel("Time")
plt.ylabel("RMS_CH1")
plt.title("RMS_CH1 over time")
plt.show()
