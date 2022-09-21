import time
from cls.cls_instrument import DeviceM
from cls.cls_write_to_file import WriteToFile


if __name__ == '__main__':
    device_m = DeviceM('instr_idn.txt')

    folder = input("Input here your folder name('d' to use default 'data'):\t")

    if folder == 'd':
        folder = 'data'
    w_2_file = WriteToFile(folder)

    for i in range(50):
        time.sleep(0.3)
        data = device_m.make_meas()
        w_2_file.record_data(data)
