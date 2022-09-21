from pathlib import Path
import pyvisa as visa


class DeviceM:
    instrument_is_open = False

    def __init__(self, cfg_file: str):
        path = str(Path(__file__))

        full_path = path[:-17] + cfg_file
        print(f'full_path: {full_path}')

        with open(full_path) as f:
            self.instrument_idn = f.read().strip()

            print(f'Setup id: {self.instrument_idn}')

        self.instrument = str()
        self.idn = 'Error'

        self.rm = visa.ResourceManager("@py")
        self.rm.list_resources()

        if self.open_instrument() != 'Ok':
            self.idn = 'Error'
        else:
            self.idn = self.query("*IDN?")
            print(self.idn)

        self.close_instrument()

    def query(self, message :str) -> str:
        if self.open_instrument() != 'Ok':
            return 'Error'

        response = message

        while message.strip() == response.strip()\
                or len(response) <= 5:
            try:
                response = self.instrument.query(message)
            except visa.VisaIOError as e:
                print(e.args)
                self.close_instrument()
                return 'Error'

        return response

    def open_instrument(self):
        if not self.instrument_is_open:
            try:
                self.instrument = self.rm.open_resource(self.instrument_idn)
                self.instrument_is_open = True
            except visa.VisaIOError as e:
                print(e.args)
                self.close_instrument()
                return 'Error'

        return 'Ok'

    def close_instrument(self):
        try:
            self.instrument.write("ROUTe:MONitor:STATe ON")
            self.instrument.write("DISPlay:TEXT:CLEar")
        except visa.VisaIOError as e:
            print(e.args)
            self.close_instrument()
        self.instrument.close()
        self.instrument_is_open = False

    def make_meas(self):

        data = self.query("MEAS?")
        return data[:-7]
