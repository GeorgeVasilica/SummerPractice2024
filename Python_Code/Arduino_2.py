import serial


class AR:
    def __init__(self, **kwargs):
        self.settings = kwargs
        self.ser = serial.Serial(self.settings['port'], 9600)
        self.voltage = 0
        self.current = 0
        self.timePython = 0
        self.ok = 0

    def send_data(self, voltage, current, is_on):
        # Format the data as a string delimited by space
        data = f"{voltage} {current} {int(is_on)} \n"
        # Send the data via serial
        self.ser.write(data.encode())

    def moment(self):  # Example of usage
        try:
            while True:
                self.is_on = True
                if self.ok == 0:
                    self.send_data(self.voltage, self.current, self.is_on)
                if self.ok == 1:
                    self.sendTime(self.voltage, self.current, self.is_on, self.timePython)
                # Wait for a while before the next send
        except KeyboardInterrupt:
            # Close the serial port upon exiting the program
            self.ser.close()

    def sendTime(self, voltage, current, is_on, timePython):
        data = f"{voltage} {current} {int(is_on)} {timePython} \n"
        # Send the data via serial
        self.ser.write(data.encode())

    def momentTime(self):
        try:
            self.sendTime(self.timePython)
            # Wait for a while before the next send
        except KeyboardInterrupt:
            # Close the serial port upon exiting the program
            self.ser.close()
