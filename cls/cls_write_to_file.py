import datetime
import time
import os
from locale import atof
from pathlib import Path


class WriteToFile:
    def __init__(self, folder_path: str):
        path = str(Path(__file__))

        # self.full_path = path[:-24] + folder_path
        self.full_path = f'.\\{folder_path}'
        print(f'full_path: {self.full_path}')

        if not os.path.isdir(self.full_path):
            print(f'Create directory {folder_path} in you data folder.')
            os.mkdir(self.full_path)

        start_date = datetime.datetime.today()
        print(f"date: {start_date}")

        self.file_name = f'{self.full_path}\\measurements_{start_date.day}.{start_date.month}.{start_date.year}_{start_date.hour}{start_date.minute}{start_date.second}.csv '
        print(f'file_name: {self.file_name}')

        with open(self.file_name, 'w') as f:
            f.writelines(f"N,Time_s,Voltage_V\n")

        self.start_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
        self.point_count = 0

    def record_data(self, data: str) -> str:

        dig_data = 0

        try:
            dig_data = atof(data)
        except ValueError:
            print('Data Value Error')
            return 'Error'

        point_time = datetime.datetime.today()
        d_time = datetime.timedelta.total_seconds(point_time - self.start_time)
        self.point_count += 1

        data_str = f'{self.point_count},{d_time},{dig_data}'

        print(f'Record measurement point. N:{self.point_count}\t time:\t{d_time}\tvalue:{dig_data}')

        with open(self.file_name, 'a') as f:
            f.write(f"{data_str}\n")

        return 'Ok'
