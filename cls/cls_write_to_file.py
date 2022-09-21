import datetime
import time
import os
from pathlib import Path


class WriteToFile:
    def __init__(self, folder_path: str):
        path = str(Path(__file__))

        self.full_path = path[:-24] + folder_path
        print(f'full_path: {self.full_path}')

        if not os.path.isdir(self.full_path):
            print(f'Create directory {folder_path} in you data folder.')
            os.mkdir(self.full_path)

        start_date = datetime.datetime.today()
        print(f"date: {start_date}")

        self.file_name = f'{self.full_path}\\measurements_{start_date.day}.{start_date.month}.{start_date.year}_{start_date.hour}{start_date.minute}{start_date.second}.txt '
        print(f'file_name: {self.file_name}')

        with open(self.file_name, 'w') as f:
            f.writelines(f"Time, s\t Voltage, V\n")

        self.start_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))

    def record_data(self, data: str):
        point_time = datetime.datetime.today()
        d_time = datetime.timedelta.total_seconds(point_time - self.start_time)
        data_str = f'{d_time}\t{data}'

        print(f'Record measurement point. time:\t{d_time}\tvalue:{data}')

        with open(self.file_name, 'a') as f:
            f.write(f"{data_str}\n")
