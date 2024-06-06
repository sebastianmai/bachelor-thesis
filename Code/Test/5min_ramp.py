import pandas as pd
import matplotlib.pyplot as plt
import glob
import matplotlib.dates as mdates
import matplotlib
from datetime import timedelta

matplotlib.use('Qt5Agg')

phyto1_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/test_5min/02/P1*.csv')
df_phyto1 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto1_files])
df_phyto1 = df_phyto1.sort_values("timestamp")

phyto2_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/test_5min/02/P4*.csv')
df_phyto2 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto2_files])
df_phyto2 = df_phyto2.sort_values("timestamp")

phyto3_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/test_5min/02/P2*.csv')
df_phyto3 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto3_files])
df_phyto3 = df_phyto3.sort_values("timestamp")

df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"], format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"], format="%Y-%m-%d %H:%M:%S:%f")
df_phyto3["timestamp"] = pd.to_datetime(df_phyto3["timestamp"], format="%Y-%m-%d %H:%M:%S:%f")

Vref = 2.5
Gain = 4
databits = 8388608

df_phyto1['Ch1'] = ((df_phyto1['Ch1'] / databits - 1) * Vref / Gain) * 1000
df_phyto2['Ch1'] = ((df_phyto2['Ch1'] / databits - 1) * Vref / Gain) * 1000
df_phyto3['Ch1'] = ((df_phyto3['Ch1'] / databits - 1) * Vref / Gain) * 1000

fig, axs = plt.subplots(3, 1, figsize=(30, 20), constrained_layout=True)

fig.suptitle("Bio potentials over time", fontsize=16, weight='bold')

axs[0].plot(df_phyto1["timestamp"], df_phyto1["Ch1"])
axs[0].set_title("Bio potential CH1 over time")
axs[0].set_ylabel("Potential [mV]")

axs[1].plot(df_phyto2["timestamp"], df_phyto2["Ch1"])
axs[1].set_title("Bio potential CH4 over time")
axs[1].set_ylabel("Potential [mV]")

axs[2].plot(df_phyto3["timestamp"], df_phyto3["Ch1"])
axs[2].set_title("Bio potential CH2 over time")
axs[2].set_ylabel("Potential [mV]")

spacing = pd.Timedelta(minutes=5)

min_timestamp = min(df_phyto1["timestamp"].min(), df_phyto2["timestamp"].min()) - spacing
max_timestamp = max(df_phyto1["timestamp"].max(), df_phyto2["timestamp"].max()) + spacing

time = min_timestamp

'''axs[0].axvline(time + timedelta(hours=1), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=1, minutes=30), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=3, minutes=30), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=4), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=6), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=6, minutes=30), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=8, minutes=30), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=9), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=11), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=11, minutes=30), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=13, minutes=30), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=14), color='g', linestyle='--')
axs[0].axvline(time + timedelta(hours=16), color='r', linestyle='--')
axs[0].axvline(time + timedelta(hours=16, minutes=30), color='g', linestyle='--')

axs[1].axvline(time + timedelta(hours=1), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=1, minutes=30), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=3, minutes=30), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=4), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=6), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=6, minutes=30), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=8, minutes=30), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=9), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=11), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=11, minutes=30), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=13, minutes=30), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=14), color='g', linestyle='--')
axs[1].axvline(time + timedelta(hours=16), color='r', linestyle='--')
axs[1].axvline(time + timedelta(hours=16, minutes=30), color='g', linestyle='--')'''

axs[0].axvline(time + timedelta(minutes=15, seconds=15), color='r', linestyle='--')
axs[0].axvline(time + timedelta(minutes=25, seconds=15), color='g', linestyle='--')
axs[1].axvline(time + timedelta(minutes=15, seconds=15), color='r', linestyle='--')
axs[1].axvline(time + timedelta(minutes=25, seconds=15), color='g', linestyle='--')
axs[2].axvline(time + timedelta(minutes=15, seconds=15), color='r', linestyle='--')
axs[2].axvline(time + timedelta(minutes=25, seconds=15), color='g', linestyle='--')

'''
time = min_timestamp
x = True
while x:
    axs[0].axvline(time + timedelta(hours=1), color='g', linestyle='--')
    axs[0].axvline(time + timedelta(hours=1, minutes=30), color='r', linestyle='--')
    axs[1].axvline(time + timedelta(hours=1), color='g', linestyle='--')
    axs[1].axvline(time + timedelta(hours=1, minutes=30), color='r', linestyle='--')

    if time < max_timestamp - timedelta(hours=2, minutes=30):
        time += timedelta(hours=2, minutes=30)
    else:
        x = False'''

for ax in axs:
    ax.set_xlim(min_timestamp, max_timestamp)
    ax.sharex(axs[0])

for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/5min_ramp02.pdf", format="pdf")
plt.show()
