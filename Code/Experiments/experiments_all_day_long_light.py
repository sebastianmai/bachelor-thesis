import asyncio

from kasa import SmartPlug
from datetime import datetime, timedelta


async def main():
    WP03 = "134.34.225.167"  # 70-4F-57-FF-AE-F5
    # WP00 = "134.34.225.132"  # D8-0D-17-5c-FC-93
    plug = WP03
    # plug = WP00
    growLight = SmartPlug(plug)
    await growLight.turn_off()
    wait_time = datetime.now()

    while (True):
        current_time = datetime.now()
        if wait_time + timedelta(hours=1) < current_time <= wait_time + timedelta(hours=1, minutes=30):
            await growLight.turn_on()
        elif wait_time + timedelta(hours=1, minutes=30) < current_time < (wait_time + timedelta(hours=2, minutes=30)):
            await growLight.turn_off()

        if current_time >= (wait_time + timedelta(hours=2, minutes=30)):
            print("new experiment")
            print(datetime.now())
            wait_time = datetime.now()

        '''if 8 <= current_time.hour <= 22:

            specific_times = [
                (8, 0),
                (10, 10),
                (12, 20),
                (14, 30),
                (16, 40),
                (18, 50)
            ]

            for hour, minute in specific_times:
                if current_time.hour == hour and minute == current_time.minute:
                    print("New ime found")
                    wait_time = datetime.now()

                    while (True):
                        current_time = datetime.now()

                        if wait_time + timedelta(minutes=60) < current_time <= wait_time + timedelta(hours=1, minutes=10):
                            await growLight.turn_on()
                        elif wait_time + timedelta(hours=1, minutes=10) < current_time < (
                                wait_time + timedelta(hours=2, minutes=10)):
                            await growLight.turn_off()

                        if current_time >= (wait_time + timedelta(hours=2, minutes=10)):
                            break'''


if __name__ == '__main__':
    asyncio.run(main())
    exit(1)
