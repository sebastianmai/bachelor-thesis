import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import glob

matplotlib.use('Qt5Agg')

#01
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/01/ACM0_2024-05-22_10:33:58.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/01/P1_2024-05-22 10:33:52:361.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/01/P2_2024-05-22 10:33:52:169.csv"

#02
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/02/ACM0_2024-05-22_11:16:47.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/02/P1_2024-05-22 11:16:39:412.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/02/P2_2024-05-22 11:16:39:242.csv"

#03
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/03/ACM0_2024-05-22_13:40:39.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/03/P1_2024-05-22 13:40:34:836.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/03/P2_2024-05-22 13:40:32:556.csv"

#04
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/ACM0_2024-05-22_14:17:02.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/P1_2024-05-22 14:16:56:438.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/P2_2024-05-22 14:16:56:308.csv"

#05
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/05/ACM0_2024-05-22_14:59:00.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/05/P1_2024-05-22 14:58:52:691.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/05/P2_2024-05-22 14:58:52:660.csv"

#06
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/06/ACM0_2024-05-22_15:46:52.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/06/P1_2024-05-22 15:46:44:810.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/06/P2_2024-05-22 15:46:44:721.csv"

#07
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/07/ACM0_2024-05-22_16:20:46.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/07/P1_2024-05-22 16:20:39:416.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/07/P2_2024-05-22 16:20:39:275.csv"

#07
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/08/ACM0_2024-05-23_13:28:54.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/08/P1_2024-05-23 13:28:47:429.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/08/P2_2024-05-23 13:28:47:401.csv"


'''
df_cybres = pd.read_csv(csv_cybres, usecols=["datetime", "RMS_CH1", "RMS_CH2", "light_external"])
df_phyto1 = pd.read_csv(csv_phyto1, usecols=["timestamp", "Ch1"])
df_phyto2 = pd.read_csv(csv_phyto2, usecols=["timestamp", "Ch1"])

df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

fig, axs = plt.subplots(5, 1, figsize=(20,10), constrained_layout=True)

fig.suptitle("Impedance amplitude bio potentials over time for wind stimulus application", fontsize=16, weight='bold')

axs[0].plot(df_cybres["datetime"], df_cybres["RMS_CH1"], color="purple")
axs[0].set_title("Impedance amplitude of CH1 over time")
axs[0].set_ylabel("RMS amplitude [$\Omega$]")

axs[1].plot(df_cybres["datetime"], df_cybres["RMS_CH2"], color="purple")
axs[1].set_title("Impedance amplitude of CH2 over time")
axs[1].set_ylabel("RMS amplitude [$\Omega$]")

axs[2].plot(df_phyto1["timestamp"], df_phyto1["Ch1"])
axs[2].set_title("Bio potential CH1 over time")
axs[2].set_ylabel("Potential [mV]")

axs[3].plot(df_phyto2["timestamp"], df_phyto2["Ch1"])
axs[3].set_title("Bio potential CH2 over time")
axs[3].set_ylabel("Potential [mV]")

axs[4].plot(df_cybres["datetime"], df_cybres["light_external"])
axs[4].set_title("Light intensity over time")
axs[4].set_ylabel("Light intensity [lux]")

n = 10

time_after_n_min_cybres = df_cybres["datetime"].min() + pd.Timedelta(minutes=n)
time_after_n_min_phyto1 = df_phyto1["timestamp"].min() + pd.Timedelta(minutes=n)
time_after_n_min_phyto2 = df_phyto2["timestamp"].min() + pd.Timedelta(minutes=n)

time_after_n_n_min_cybres = df_cybres["datetime"].min() + pd.Timedelta(minutes=n+n)
time_after_n_n_min_phyto1 = df_phyto1["timestamp"].min() + pd.Timedelta(minutes=n+n)
time_after_n_n_min_phyto2 = df_phyto2["timestamp"].min() + pd.Timedelta(minutes=n+n)
axs[0].axvline(time_after_n_min_cybres, color='r', linestyle='--')
axs[1].axvline(time_after_n_min_cybres, color='r', linestyle='--')
axs[2].axvline(time_after_n_min_phyto1, color='r', linestyle='--')
axs[3].axvline(time_after_n_min_phyto2, color='r', linestyle='--')
axs[4].axvline(time_after_n_min_phyto2, color='r', linestyle='--')

axs[0].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
axs[1].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
axs[2].axvline(time_after_n_n_min_phyto1, color='r', linestyle='--')
axs[3].axvline(time_after_n_n_min_phyto2, color='r', linestyle='--')
axs[4].axvline(time_after_n_min_phyto2, color='r', linestyle='--')

for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/red_test_08.pdf", format="pdf")
plt.show()'''


acm0_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/ACM0*.csv')
df_cybres = pd.concat([pd.read_csv(f, usecols=["datetime", "RMS_CH1", "RMS_CH2", "light_external"]) for f in acm0_files])
df_cybres = df_cybres.sort_values("datetime")

phyto1_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P1*.csv')
df_phyto1 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto1_files])
df_phyto1 = df_phyto1.sort_values("timestamp")

phyto2_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P2*.csv')
df_phyto2 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto2_files])
df_phyto2 = df_phyto2.sort_values("timestamp")

phyto3_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P3*.csv')
df_phyto3 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto3_files])
df_phyto3 = df_phyto3.sort_values("timestamp")

phyto4_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P4*.csv')
df_phyto4 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto4_files])
df_phyto4 = df_phyto4.sort_values("timestamp")

phyto5_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P5*.csv')
df_phyto5 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto5_files])
df_phyto5 = df_phyto5.sort_values("timestamp")

phyto6_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/27/P6*.csv')
df_phyto6 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"]) for f in phyto6_files])
df_phyto6 = df_phyto6.sort_values("timestamp")

df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto3["timestamp"] = pd.to_datetime(df_phyto3["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto4["timestamp"] = pd.to_datetime(df_phyto4["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto5["timestamp"] = pd.to_datetime(df_phyto5["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto6["timestamp"] = pd.to_datetime(df_phyto6["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

fig, axs = plt.subplots(9, 1, figsize=(30,20), constrained_layout=True)

fig.suptitle("Impedance amplitude bio potentials over time for red stimulus application", fontsize=16, weight='bold')

axs[0].plot(df_cybres["datetime"], df_cybres["RMS_CH1"], color="purple")
axs[0].set_title("Impedance amplitude of CH1 over time")
axs[0].set_ylabel("RMS amplitude [$\Omega$]")

axs[1].plot(df_cybres["datetime"], df_cybres["RMS_CH2"], color="purple")
axs[1].set_title("Impedance amplitude of CH2 over time")
axs[1].set_ylabel("RMS amplitude [$\Omega$]")

axs[2].plot(df_phyto1["timestamp"], df_phyto1["Ch1"])
axs[2].set_title("Bio potential CH1 over time")
axs[2].set_ylabel("Potential [mV]")

axs[3].plot(df_phyto2["timestamp"], df_phyto2["Ch1"])
axs[3].set_title("Bio potential CH2 over time")
axs[3].set_ylabel("Potential [mV]")

axs[4].plot(df_phyto3["timestamp"], df_phyto3["Ch1"])
axs[4].set_title("Bio potential CH3 over time")
axs[4].set_ylabel("Potential [mV]")

axs[5].plot(df_phyto4["timestamp"], df_phyto4["Ch1"])
axs[5].set_title("Bio potential CH4 over time")
axs[5].set_ylabel("Potential [mV]")

axs[6].plot(df_phyto5["timestamp"], df_phyto5["Ch1"])
axs[6].set_title("Bio potential CH5 over time")
axs[6].set_ylabel("Potential [mV]")

axs[7].plot(df_phyto6["timestamp"], df_phyto6["Ch1"])
axs[7].set_title("Bio potential CH6 over time")
axs[7].set_ylabel("Potential [mV]")

axs[8].plot(df_cybres["datetime"], df_cybres["light_external"])
axs[8].set_title("Light intensity over time")
axs[8].set_ylabel("Light intensity [lux]")

spacing = pd.Timedelta(minutes=5)

min_timestamp = min(df_cybres["datetime"].min(), df_phyto1["timestamp"].min(), df_phyto2["timestamp"].min()) - spacing
max_timestamp = max(df_cybres["datetime"].max(), df_phyto1["timestamp"].max(), df_phyto2["timestamp"].max()) + spacing

for ax in axs:
    ax.set_xlim(min_timestamp, max_timestamp)
    ax.sharex(axs[0])


for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/test_red27.pdf", format="pdf")
plt.show()