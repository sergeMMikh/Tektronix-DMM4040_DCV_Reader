import time
from cls.cls_instrument import DeviceM
from cls.cls_write_to_file import WriteToFile


if __name__ == '__main__':
    device_m = DeviceM('instr_idn.txt')

    w_2_file = WriteToFile('data')

    for i in range(5):
        time.sleep(0.3)
        data = device_m.make_meas()
        w_2_file.record_data(data)
