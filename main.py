import time
from cls.cls_instrument import DeviceM
from cls.cls_write_to_file import WriteToFile


if __name__ == '__main__':

    try:
        with open('instr_idn.txt') as f:
            instrument_idn = f.read().strip()

            print(f'Setup id: {instrument_idn}')
    except:
        print('File "instr_idn.txt" not found.')
        instrument_idn = ''

    folder = input("Input here your folder name('d' to use default 'data'):\t")

    device_m = DeviceM(instrument_idn)



    if folder == 'd':
        folder = 'data'
    w_2_file = WriteToFile(folder)

    while True:
        time.sleep(0.3)
        data = device_m.make_meas()
        w_2_file.record_data(data)
