import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import glob

matplotlib.use('Qt5Agg')

#01
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/ACM0_2024-05-15_14:18:35.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/P1_2024-05-15 14:18:39:645.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/01/P2_2024-05-15 14:18:34:979.csv"

#02
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/ACM0_2024-05-16_10:06:47.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P1_2024-05-16 10:06:52:045.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P2_2024-05-16 10:06:51:993.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/02/P6_2024-05-16 10:06:54:932880.csv"

#03
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/03/ACM0_2024-05-17_10:16:30.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/03/P1_2024-05-17 10:16:35:105.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/03/P2_2024-05-17 10:16:33:231.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/03/P6_2024-05-17 10:16:37:949993.csv"

#04
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/04/ACM0_2024-05-17_11:02:35.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/04/P1_2024-05-17 11:02:27:909.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/04/P2_2024-05-17 11:02:27:836.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/04/P6_2024-05-17 11:02:27:708956.csv"

#05
'''
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/ACM0_2024-05-17_11:41:23.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/P1_2024-05-17 11:41:23:435.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/P2_2024-05-17 11:41:16:868.csv"
csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/P6_2024-05-17 11:41:15:615919.csv"
csv_cybres1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/ACM0_2024-05-17_12:00:01.csv"
csv_phyto11 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/P1_2024-05-17 12:00:00:007.csv"
csv_phyto21 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/05/P2_2024-05-17 12:00:00:210.csv"

df_cybres1 = pd.read_csv(csv_cybres1, usecols=["datetime", "RMS_CH1", "RMS_CH2", "temp_external"])
df_phyto11 = pd.read_csv(csv_phyto11, usecols=["timestamp", "Ch1"])
df_phyto21 = pd.read_csv(csv_phyto21, usecols=["timestamp", "Ch1"])'''

#06
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/06/ACM0_2024-05-17_14:09:44.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/06/P1_2024-05-17 14:09:36:677.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/06/P2_2024-05-17 14:09:36:547.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/06/P6_2024-05-17 14:09:36:630648.csv"

#07
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/07/ACM0_2024-05-17_14:59:49.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/07/P1_2024-05-17 14:59:41:658.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/07/P2_2024-05-17 14:59:41:541.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/07/P6_2024-05-17 14:59:41:413469.csv"

#08
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/08/ACM0_2024-05-17_15:34:07.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/08/P1_2024-05-17 15:34:00:820.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/08/P2_2024-05-17 15:34:00:798.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/08/P6_2024-05-17 15:34:00:419496.csv"

#Long heatup
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup/ACM0_2024-05-21_17:26:39.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup/P1_2024-05-21 17:26:32:286.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup/P2_2024-05-21 17:26:31:802.csv"
csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup/P6_2024-05-21 17:26:31:458540.csv"

#Long heatup 2
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_02/ACM0_2024-05-22_17:45:11.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_02/P1_2024-05-22 17:45:04:304.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_02/P2_2024-05-22 17:45:03:966.csv"
csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_02/P6_2024-05-22 17:45:03:671442.csv"
csv_switches = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_02/state_changes.csv"

#Long heatup 3
csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_03/ACM0_2024-05-23_17:24:37.csv"
csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_03/P1_2024-05-23 17:24:30:456.csv"
csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_03/P2_2024-05-23 17:24:30:855.csv"
csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_03/P6_2024-05-23 17:24:29:691779.csv"
csv_switches = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long_heatup_03/state_changes.csv"

#control_measure_01
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/ACM0_2024-05-16_11:37:45.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P1_2024-05-16 11:37:48:302.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P2_2024-05-16 11:37:43:099.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure/P6_2024-05-16 11:37:52:714979.csv"


#control_measure_02
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
#csv_cybres = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/ACM0_2024-05-16_16:41:25.csv"
#csv_phyto1 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P1_2024-05-16 16:41:22:783.csv"
#csv_phyto2 = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P2_2024-05-16 16:41:22:292.csv"
#csv_temp = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/control_measure_04/P6_2024-05-16 16:41:23:434158.csv"

'''df_cybres = pd.read_csv(csv_cybres, usecols=["datetime", "RMS_CH1", "RMS_CH2"])
df_phyto1 = pd.read_csv(csv_phyto1, usecols=["timestamp", "Ch1"])
df_phyto2 = pd.read_csv(csv_phyto2, usecols=["timestamp", "Ch1"])
df_temp = pd.read_csv(csv_temp)
df_switches = pd.read_csv(csv_switches)

print(df_switches)



#df_cybres = pd.concat([df_cybres, df_cybres1])
#df_phyto1 = pd.concat([df_phyto1, df_phyto11])
#df_phyto2 = pd.concat([df_phyto2, df_phyto21])
#print(df_cybres)

#df_phyto1 = df_phyto1.iloc[::100, :]
#df_phyto2 = df_phyto2.iloc[::100, :]
#df_temp = df_temp.iloc[::100, :]'''

'''
base_path = "/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/Long"
files3 = [
    f"{base_path}/ACM0_2024-05-17_16:40:10.csv",
    f"{base_path}/ACM0_2024-05-18_00:00:00.csv",
    f"{base_path}/ACM0_2024-05-18_12:00:00.csv",
    f"{base_path}/ACM0_2024-05-19_00:00:00.csv",
    f"{base_path}/ACM0_2024-05-19_12:00:01.csv",
    f"{base_path}/ACM0_2024-05-20_00:00:00.csv"
]

files = [
    f"{base_path}/P2_2024-05-17 16:40:03:005.csv",
    f"{base_path}/P2_2024-05-18 00:00:00:103.csv",
    f"{base_path}/P2_2024-05-18 12:00:00:032.csv",
    f"{base_path}/P2_2024-05-19 00:00:00:056.csv",
    f"{base_path}/P2_2024-05-19 12:00:00:046.csv",
    f"{base_path}/P2_2024-05-20 00:00:00:006.csv"
]

files1 = [
    f"{base_path}/P1_2024-05-17 16:40:03:100.csv",
    f"{base_path}/P1_2024-05-18 00:00:00:034.csv",
    f"{base_path}/P1_2024-05-18 12:00:00:067.csv",
    f"{base_path}/P1_2024-05-19 00:00:00:011.csv"
]

files2 = [
    f"{base_path}/P6_2024-05-17 16:40:02:530802.csv",
    f"{base_path}/P6_2024-05-18 00:00:03:884.csv",
    f"{base_path}/P6_2024-05-18 14:00:00:455.csv",
    f"{base_path}/P6_2024-05-19 00:00:00:660.csv"
]

dfs = [pd.read_csv(file) for file in files3]
df_cybres = pd.concat(dfs, ignore_index=True)

dfs = [pd.read_csv(file) for file in files]
df_phyto2 = pd.concat(dfs, ignore_index=True)


dfs = [pd.read_csv(file) for file in files1]
df_phyto1 = pd.concat(dfs, ignore_index=True)

dfs = [pd.read_csv(file) for file in files2]
df_temp = pd.concat(dfs, ignore_index=True)'''

'''
df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_temp["timestamp"] = pd.to_datetime(df_temp["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

min_timestamp = min(df_cybres["datetime"].min(), df_phyto1["timestamp"].min(), df_phyto2["timestamp"].min(), df_temp["timestamp"].min())

delta = min_timestamp + pd.Timedelta(hours=4)

df_cybres = df_cybres.loc[df_cybres['datetime'] <= delta]
df_phyto1 = df_phyto1.loc[df_phyto1['timestamp'] <= delta]
df_phyto2 = df_phyto2.loc[df_phyto2['timestamp'] <= delta]
df_temp = df_temp.loc[df_temp['timestamp'] <= delta]


fig, axs = plt.subplots(6, 1, figsize=(20,10), constrained_layout=True)

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
axs[3].set_ylabel("Potential [mV]")'''

'''
axs[3].plot(df_cybres["datetime"], df_cybres["temp_external"], color="red")
axs[3].set_title("Temperature over time")
axs[3].set_ylabel("temp [°C]")
'''

'''
axs[4].plot(df_temp["timestamp"], df_temp["T1_leaf"], label="leaf low")
axs[4].plot(df_temp["timestamp"], df_temp["T2_leaf"], label="leaf high")
axs[4].plot(df_temp["timestamp"], df_temp["T1_air"], label="air low")
axs[4].plot(df_temp["timestamp"], df_temp["T2_air"], label="air high")
axs[4].set_title("Temperature over time")
axs[4].set_ylabel("temp [°C]")
axs[4].legend()

#n = 60

#time_after_n_min_cybres = df_cybres["datetime"].min() + pd.Timedelta(minutes=n)
#time_after_n_min_phyto1 = df_phyto1["timestamp"].min() + pd.Timedelta(minutes=n)
#time_after_n_min_phyto2 = df_phyto2["timestamp"].min() + pd.Timedelta(minutes=n)
#time_after_n_min_temp = df_temp["timestamp"].min() + pd.Timedelta(minutes=n)

#time_after_n_n_min_cybres = df_cybres["datetime"].min() + pd.Timedelta(minutes=n+10)
#time_after_n_n_min_phyto1 = df_phyto1["timestamp"].min() + pd.Timedelta(minutes=n+n)
#time_after_n_n_min_phyto2 = df_phyto2["timestamp"].min() + pd.Timedelta(minutes=n+n)
#time_after_n_n_min_temp = df_temp["timestamp"].min() + pd.Timedelta(minutes=n+n)

#axs[0].axvline(time_after_n_min_cybres, color='r', linestyle='--')
#axs[1].axvline(time_after_n_min_cybres, color='r', linestyle='--')
#axs[2].axvline(time_after_n_min_phyto1, color='r', linestyle='--')
#axs[3].axvline(time_after_n_min_phyto2, color='r', linestyle='--')
#axs[4].axvline(time_after_n_min_temp, color='r', linestyle='--')

#axs[0].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
#axs[1].axvline(time_after_n_n_min_cybres, color='r', linestyle='--')
#axs[2].axvline(time_after_n_n_min_phyto1, color='r', linestyle='--')
#axs[3].axvline(time_after_n_n_min_phyto2, color='r', linestyle='--')
#axs[4].axvline(time_after_n_n_min_temp, color='r', linestyle='--')

var = 1
axs[5].set_title("Switches on/off over time")

for index, row in df_switches.iterrows():
    if row.iloc[1] == "on" and var == 1:
        axs[5].axvline(pd.to_datetime(row.iloc[0]), color='g', linestyle='--')
        var = 0
    elif var == 0:
        axs[5].axvline(pd.to_datetime(row.iloc[0]), color='r', linestyle='--')
        var = 1


spacing = pd.Timedelta(minutes=30)

min_timestamp = min(df_cybres["datetime"].min(), df_phyto1["timestamp"].min(), df_phyto2["timestamp"].min(), df_temp["timestamp"].min()) - spacing
max_timestamp = max(df_cybres["datetime"].max(), df_phyto1["timestamp"].max(), df_phyto2["timestamp"].max(), df_temp["timestamp"].max()) + spacing

for ax in axs:
    ax.set_xlim(min_timestamp, max_timestamp)

for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/heat_test_long_heatup_03.pdf", format="pdf")
plt.show()'''

def skip_rows(index):
    return index % 1000 != 0

N = 1000

acm0_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/ACM0*.csv')

df_cybres = pd.concat([pd.read_csv(f, usecols=["datetime", "RMS_CH1", "RMS_CH2", "temp_external"], skiprows=lambda i: i % N) for f in acm0_files])
df_cybres = df_cybres.sort_values("datetime")
#df_cybres = df_cybres.iloc[::1000, :]

phyto1_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P1*.csv')
df_phyto1 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"],  skiprows=lambda i: i % N) for f in phyto1_files])
df_phyto1 = df_phyto1.sort_values("timestamp")
#df_phyto1 = df_phyto1.iloc[::1000, :]

phyto2_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P2*.csv')
df_phyto2 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"],  skiprows=lambda i: i % N) for f in phyto2_files])
df_phyto2 = df_phyto2.sort_values("timestamp")
#df_phyto2 = df_phyto2.iloc[::1000, :]

phyto3_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P3*.csv')
df_phyto3 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"],  skiprows=lambda i: i % N) for f in phyto3_files])
df_phyto3 = df_phyto3.sort_values("timestamp")
#df_phyto3 = df_phyto3.iloc[::1000, :]

phyto4_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P4*.csv')
df_phyto4 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"], skiprows=lambda i: i % N) for f in phyto4_files])
df_phyto4 = df_phyto4.sort_values("timestamp")
#df_phyto4 = df_phyto4.iloc[::1000, :]

phyto5_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P5*.csv')
df_phyto5 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"], skiprows=lambda i: i % N) for f in phyto5_files])
df_phyto5 = df_phyto5.sort_values("timestamp")
#df_phyto5 = df_phyto5.iloc[::1000, :]

phyto6_files = glob.glob('/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/Data/Test_measurement_heat/bad heat/P6*.csv')
df_phyto6 = pd.concat([pd.read_csv(f, usecols=["timestamp", "Ch1"], skiprows=lambda i: i % N) for f in phyto6_files])
df_phyto6 = df_phyto6.sort_values("timestamp")
#df_phyto6 = df_phyto6.iloc[::1000, :]

df_cybres["datetime"] = pd.to_datetime(df_cybres["datetime"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto1["timestamp"] = pd.to_datetime(df_phyto1["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto2["timestamp"] = pd.to_datetime(df_phyto2["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto3["timestamp"] = pd.to_datetime(df_phyto3["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto4["timestamp"] = pd.to_datetime(df_phyto4["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto5["timestamp"] = pd.to_datetime(df_phyto5["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")
df_phyto6["timestamp"] = pd.to_datetime(df_phyto6["timestamp"],  format="%Y-%m-%d %H:%M:%S:%f")

fig, axs = plt.subplots(9, 1, figsize=(30,20), constrained_layout=True)

fig.suptitle("Impedance amplitude and bio potentials over time for heat stimulus application", fontsize=16, weight='bold')

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

axs[5].plot(df_phyto3["timestamp"], df_phyto3["Ch1"])
axs[5].set_title("Bio potential CH3 over time")
axs[5].set_ylabel("Potential [mV]")

axs[6].plot(df_phyto4["timestamp"], df_phyto4["Ch1"])
axs[6].set_title("Bio potential CH4 over time")
axs[6].set_ylabel("Potential [mV]")

axs[4].plot(df_phyto5["timestamp"], df_phyto5["Ch1"])
axs[4].set_title("Bio potential CH5 over time")
axs[4].set_ylabel("Potential [mV]")

axs[7].plot(df_phyto6["timestamp"], df_phyto6["Ch1"])
axs[7].set_title("Bio potential CH6 over time")
axs[7].set_ylabel("Potential [mV]")

axs[8].plot(df_cybres["datetime"], df_cybres["temp_external"])
axs[8].set_title("Temperature over time")
axs[8].set_ylabel("temp [°C]")


spacing = pd.Timedelta(minutes=5)

min_timestamp = min(df_cybres["datetime"].min(), df_phyto1["timestamp"].min(), df_phyto2["timestamp"].min()) - spacing
max_timestamp = max(df_cybres["datetime"].max(), df_phyto1["timestamp"].max(), df_phyto2["timestamp"].max()) + spacing



for ax in axs:
    ax.set_xlim(min_timestamp, max_timestamp)
    ax.sharex(axs[0])


for ax in axs:
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.savefig("/home/basti/DATEN/Universität/Bachelor/Thesis/bachelor-thesis/RESULTS/Plots/bad_heat.pdf", format="pdf")
plt.show()





