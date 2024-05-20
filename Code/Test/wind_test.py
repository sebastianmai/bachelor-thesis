import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

matplotlib.use('Qt5Agg')

#01
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/01/ACM0_2024-05-20_12:07:10.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/01/P1_2024-05-20 12:07:02:585.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/01/P2_2024-05-20 12:07:02:094.csv"

#02
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/02/ACM0_2024-05-20_13:23:11.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/02/P1_2024-05-20 13:23:04:097.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/02/P2_2024-05-20 13:23:03:910.csv"

#03
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/03/ACM0_2024-05-20_14:35:04.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/03/P1_2024-05-20 14:34:56:749.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/03/P2_2024-05-20 14:34:56:626.csv"

#04
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/04/ACM0_2024-05-20_15:16:29.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/04/P1_2024-05-20 15:16:22:204.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/04/P2_2024-05-20 15:16:22:061.csv"

#05
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/05/ACM0_2024-05-20_15:52:53.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/05/P1_2024-05-20 15:52:45:532.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_wind/05/P2_2024-05-20 15:52:45:437.csv"

df_cybres = pd.read_csv(csv_cybres, usecols=["datetime", "RMS_CH1", "RMS_CH2", "temp_external"])
df_phyto1 = pd.read_csv(csv_phyto1, usecols=["timestamp", "Ch1"])
df_phyto2 = pd.read_csv(csv_phyto2, usecols=["timestamp", "Ch1"])

df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

fig, axs = plt.subplots(4, 1, figsize=(20,10), constrained_layout=True)

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
axs[0].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
axs[1].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
axs[2].axvline(time_after_n_n_min_phyto1, color='r', linestyle='--')
axs[3].axvline(time_after_n_n_min_phyto2, color='r', linestyle='--')

for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/wind_test_05.pdf", format="pdf")
plt.show()