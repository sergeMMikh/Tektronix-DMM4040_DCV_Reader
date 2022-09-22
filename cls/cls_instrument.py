from pathlib import Path
import pyvisa as visa


class DeviceM:
    instrument_is_open = False

    def __init__(self, instrument_idn: str):
        self.instrument_idn = instrument_idn

        self.instrument = str()
        self.idn = 'Error'

        self.rm = visa.ResourceManager("@py")
        self.rm.list_resources()

        print(f'instrument_idn: {self.instrument_idn}')

        if self.open_instrument() != 'Ok':
            self.idn = 'Error'
            print('Error in open instrument.')
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
        self.instrument.close()
        self.instrument_is_open = False

    def make_meas(self):

        data = self.query("MEAS?")
        return data[:-7]
