import asyncio

from kasa import SmartPlug
from datetime import datetime, timedelta
import pandas as pd
import os
import time
import csv

scaling_factors = {
    "temp-external": lambda t: t / 10000,
    "humidity-external": lambda t: t / 1,
    # actual function should be ((x * 3 / 4200000-0.1515) / (0.006707256-0.0000137376 * (temp-external / 10000.0)))
    "light-external": lambda t: (t / 799.4) - 0.75056,
    "differential_potential_CH1": lambda t: (t - 512000) / 1000,
    "differential_potential_CH2": lambda t: (t - 512000) / 1000,
    "transpiration": lambda t: t / 1000,
    "soil_moisture": lambda t: t,
    "soil_temperature": lambda t: t / 10
}

path = '/home/pi/Measurements'

async def main():

    WP03 = "134.34.225.167"  # 70-4F-57-FF-AE-F5

    #WP00 = "134.34.225.132"
    plug = WP03
    growLight = SmartPlug(plug)
    await growLight.turn_off()

    #wait_time = datetime.now()
    start_temp = get_temp(0)

    while True:
        current_time = datetime.now()

        specific_times = [
            (8, 0),
            (10, 10),
            (12, 20),
            (14, 30),
            (16, 40),
            (18, 50),
        ]
        '''if wait_time + timedelta(hours=1) < current_time <= wait_time + timedelta(hours=3):
            print("stimulus started")
            current_temp = get_temp(-1)

            if current_temp[2] <= start_temp[2] + 7:
                await growLight.turn_on()
                log_state_change('on')
                time.sleep(3)
            elif current_temp[2] > start_temp[2] + 7:
                await growLight.turn_off()
                log_state_change('off')
                time.sleep(3)
        elif wait_time + timedelta(hours=3) < current_time <= wait_time + timedelta(hours=4):
            print("turned off")
            await growLight.turn_off()

        if current_time >= (wait_time + timedelta(hours=4)):
            print('Broken')
            break'''



control_heat
        for hour, minute in specific_times:
            if current_time.hour == hour and minute == current_time.minute:
                print('Time found')
                wait_time = datetime.now()
                start_temp = get_temp(0)

                while True:
                    current_time = datetime.now()

                    if wait_time + timedelta(minutes=60) < current_time <= wait_time + timedelta(hours=1, minutes=10):
                        current_temp = get_temp(-1)

                        if current_temp <= start_temp + 6:
                            await growLight.turn_on()
                            time.sleep(3)
                        elif current_temp <= start_temp + 6:
                            await growLight.turn_off()
                            time.sleep(3)
                    elif wait_time + timedelta(hours=1, minutes=10) < current_time <= (
                            wait_time + timedelta(hours=2, minutes=10)):
                        await growLight.turn_off()

                    if current_time >= (wait_time + timedelta(hours=2, minutes=10)):
                        print('Broken')
                        break

                print('Searching')

    '''while (True):

        current_time = datetime.now()
        if wait_time + timedelta(minutes=10) < current_time <= wait_time + timedelta(minutes=20):
            current_temp = get_temp(-1)
            print(current_temp[0], current_temp[1], current_temp[2], current_temp[3])
            growLight.turn_on()
            time.sleep(1)
        elif wait_time + timedelta(minutes=20) < current_time <= (wait_time + timedelta(minutes=30)):
            print("Turned off")
            growLight.turn_off()
        elif current_time > (wait_time + timedelta(minutes=20)):
            print("Exit the code")
            break
        


        if wait_time + timedelta(minutes=10) < current_time <= wait_time + timedelta(minutes=20):
            current_temp = get_temp(-1)
            print(current_temp[0], current_temp[1], current_temp[2], current_temp[3])

            if current_temp[2] <= start_temp[2] + 6:
                growLight.turn_on()
                time.sleep(1)
            elif current_temp[2] > start_temp[2] + 6:
                growLight.turn_off()
                time.sleep(1)
        elif wait_time + timedelta(minutes=20) < current_time <= (wait_time + timedelta(minutes=30)):
            growLight.turn_off()
        elif current_time > (wait_time + timedelta(minutes=20)):
            break

        current_time = datetime.now()

        if wait_time + timedelta(minutes=5) >= current_time:
            growLight.turn_off()
            time.sleep(1)
        elif wait_time + timedelta(minutes=5) < current_time <= wait_time + timedelta(minutes=15):
            current_temp = get_temp(-1)
            print(current_temp[0], current_temp[1], current_temp[2], current_temp[3])
            growLight.turn_on()
        else:
            growLight.turn_off()
            time.sleep(1)
            exit(1)

        if current_temp[3] >= 45 or current_temp[1] >= 40:
            growLight.turn_off()
            time.sleep(1)
            exit(1)
        '''


def get_temp(position):
    folder_path = '/home/pi/measurements/'
    files = os.listdir(folder_path)
    full_name = [os.path.join(folder_path, file) for file in files]
    sorted_files = sorted(full_name, key=os.path.getmtime, reverse=True)
    temp = pd.read_csv(sorted_files[0])

    temp["temp_external"] = scaling_factors["temp_external"](temp["temp_external"])
    last_temp = temp["temp_external"].iloc[position]

    return last_temp

    #data_cybres["temp_external"] = scaling_factors["temp_external"](data_cybres["temp_external"])
    '''last_temp_T1_leaf = temp["T1_leaf"].iloc[position]
    last_temp_T2_leaf = temp["T2_leaf"].iloc[position]
    last_temp_T1_air = temp["T1_air"].iloc[position]
    last_temp_T2_air = temp["T2_air"].iloc[position]

    return (last_temp_T1_leaf, last_temp_T1_air, last_temp_T2_leaf, last_temp_T2_air)'''

def log_state_change(state):
    filename = os.path.join(path, 'state_changes.csv')
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), state])

if __name__ == '__main__':
    asyncio.run(main())
