import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

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

#03
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/ACM0_2024-05-22_14:17:02.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/P1_2024-05-22 14:16:56:438.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_red/04/P2_2024-05-22 14:16:56:308.csv"


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
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/red_test_05.pdf", format="pdf")
plt.show()