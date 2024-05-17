import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

matplotlib.use('Qt5Agg')


#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/ACM0_2024-05-16_10:06:47.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P1_2024-05-16 10:06:52:045.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P2_2024-05-16 10:06:51:993.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P6_2024-05-16 10:06:54:932880.csv"

#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/ACM0_2024-05-15_14:18:35.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/P1_2024-05-15 14:18:39:645.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/P2_2024-05-15 14:18:34:979.csv"

# control_measure_01
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/ACM0_2024-05-16_11:37:45.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P1_2024-05-16 11:37:48:302.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P2_2024-05-16 11:37:43:099.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P6_2024-05-16 11:37:52:714979.csv"


# control_measure_02
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_02/ACM0_2024-05-16_14:17:49.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_02/P1_2024-05-16 14:17:49:189.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_02/P2_2024-05-16 14:17:46:004.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_02/P6_2024-05-16 14:17:50:919535.csv"

#control_measure_03
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_03/ACM0_2024-05-16_16:12:30.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_03/P1_2024-05-16 16:12:35:486.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_03/P2_2024-05-16 16:12:29:034.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_03/P6_2024-05-16 16:12:34:604266.csv"

#control_measure_04
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/ACM0_2024-05-16_16:41:25.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P1_2024-05-16 16:41:22:783.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P2_2024-05-16 16:41:22:292.csv"
csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P6_2024-05-16 16:41:23:434158.csv"


df_cybres = pd.read_csv(csv_cybres, usecols=["datetime", "RMS_CH1", "RMS_CH2", "temp_external"])
df_phyto1 = pd.read_csv(csv_phyto1, usecols=["timestamp", "Ch1"])
df_phyto2 = pd.read_csv(csv_phyto2, usecols=["timestamp", "Ch1"])
df_temp = pd.read_csv(csv_temp)

print(df_cybres)
#df_phyto1 = df_phyto1.iloc[::100, :]
#df_phyto2 = df_phyto2.iloc[::100, :]
#df_temp = df_temp.iloc[::100, :]


df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_temp["timestamp"] = pd.to_datetime(df_temp["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

fig, axs = plt.subplots(5, 1, figsize=(20,10), constrained_layout=True)

fig.suptitle("Impedance amplitude, bio potentials and temperature over time", fontsize=16, weight='bold')

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

'''
axs[3].plot(df_cybres["datetime"], df_cybres["temp_external"], color="red")
axs[3].set_title("Temperature over time")
axs[3].set_ylabel("temp [°C]")'''


axs[4].plot(df_temp["timestamp"], df_temp["T1_leaf"], label="leaf low")
axs[4].plot(df_temp["timestamp"], df_temp["T2_leaf"], label="leaf high")
axs[4].plot(df_temp["timestamp"], df_temp["T1_air"], label="air low")
axs[4].plot(df_temp["timestamp"], df_temp["T2_air"], label="air high")
axs[4].set_title("Temperature over time")
axs[4].set_ylabel("temp [°C]")
axs[4].legend()


time_after_5_min_cybres = df_cybres["datetime"].min() + pd.Timedelta(minutes=5)
time_after_5_min_phyto1 = df_phyto1["timestamp"].min() + pd.Timedelta(minutes=5)
time_after_5_min_phyto2 = df_phyto2["timestamp"].min() + pd.Timedelta(minutes=5)
time_after_5_min_temp = df_temp["timestamp"].min() + pd.Timedelta(minutes=5)

axs[0].axvline(time_after_5_min_cybres, color='r', linestyle='--')
axs[1].axvline(time_after_5_min_cybres, color='r', linestyle='--')
axs[2].axvline(time_after_5_min_phyto1, color='r', linestyle='--')
axs[3].axvline(time_after_5_min_phyto2, color='r', linestyle='--')
axs[4].axvline(time_after_5_min_temp, color='r', linestyle='--')

for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/heat_control_04.pdf", format="pdf")
plt.show()


