import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import glob
from matplotlib.ticker import MaxNLocator
from matplotlib.dates import DateFormatter

matplotlib.use('Qt5Agg')

csv_file = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_sensors/measurements (46285)"

csv_files = glob.glob(csv_file + "/*.csv")
dfs = []
for filename in csv_files:
    df = pd.read_csv(filename, usecols=["datetime", "sweep_freq", "RMS_CH1"])
    dfs.append(df)
combined_df = pd.concat(dfs, ignore_index=True)


drop_indices = []
for i in range(0, len(combined_df)-1):
    if combined_df.loc[i, "sweep_freq"] == combined_df.loc[i+1, "sweep_freq"]:
        drop_indices.append(i+1)
combined_df.drop(drop_indices, inplace=True)
combined_df.reset_index(drop=True, inplace=True)
combined_df["datetime"] = pd.to_datetime(combined_df["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")

start_index = 0
dfs = []
timestamps = []
for i in range(len(combined_df)):
    if combined_df.loc[i, "sweep_freq"] == 10000:
        dfs.append(combined_df.loc[start_index:i])
        timestamps.append(combined_df.loc[i, "datetime"])
        start_index = i+1
timestamps = sorted(timestamps)

if start_index < len(combined_df):
    dfs.append(combined_df.loc[start_index:])

'''
heatmap_data = np.zeros((len(dfs), len(dfs[0])))
for i, df in enumerate(dfs):
    heatmap_data[i, :] = df['RMS_CH1'].values
plt.figure(figsize=(20, 10))
plt.imshow(heatmap_data, aspect='auto', cmap='hot', origin='lower')
cbar = plt.colorbar(label='RMS_CH1')
cbar.set_label('RMS_CH1', labelpad=20)
plt.ylabel('Sweep', labelpad=20)
plt.xlabel('Frequency [Hz]', labelpad=20)
plt.title('Heatmap of RMS_CH1')
frequencies = np.ceil(dfs[0]['sweep_freq'].values/10).astype(int)
plt.xticks(np.arange(len(frequencies)), frequencies)
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(nbins=10))

ax = plt.gca()
ax.yaxis.set_major_formatter(DateFormatter("%Y-%m-%d %H:%M"))
formatted_timestamps = [ts.strftime("%Y-%m-%d %H:%M") for ts in timestamps]
plt.yticks(np.arange(len(timestamps)), formatted_timestamps)
ax.yaxis.set_major_locator(MaxNLocator(nbins=5))



plt.savefig('heatmat_impedance.pdf', format="pdf")
plt.show()'''


ax = plt.figure(figsize=(20, 10)).add_subplot(projection='3d')
for i, df in enumerate(dfs):
    ax.scatter([i]*len(df), df['sweep_freq']/10, df['RMS_CH1'])

ax.set_xlabel('Sweep')
ax.set_ylabel('Frequency [Hz]')
ax.set_zlabel('RMS_CH1')

ax = plt.gca()
ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d %H:%M"))
formatted_timestamps = [ts.strftime("%Y-%m-%d %H:%M") for ts in timestamps]
plt.xticks(np.arange(len(timestamps)), formatted_timestamps)
ax.xaxis.set_major_locator(MaxNLocator(nbins=5))

plt.savefig('plot.pdf', format="pdf")
plt.show()


'''
plt.figure(figsize=(10, 5))

start_index = 0
dfs = []
for i in range(len(combined_df)):
    if combined_df.loc[i, "sweep_freq"] == 10000:
        dfs.append(combined_df.loc[start_index:i])
        start_index = i+1

dfs.append(combined_df.loc[start_index:])

colors = ['blue', 'red', 'green', 'orange', 'purple', 'cyan']
for i, item in enumerate(dfs):
    color = colors[i % len(colors)]
    plt.plot(item["sweep_freq"]/10, item["RMS_CH1"], color=color)
plt.xlabel("Frequency [Hz]")
plt.ylabel("RMS_CH1")
plt.title("RMS_CH1 over time")
plt.show()'''



