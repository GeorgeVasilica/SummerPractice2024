import tkinter as tk
from tkinter import ttk
import Arduino_2 as AR
import serial.tools.list_ports
import threading
from time import sleep

# Event to signal threads to stop
stop_event = threading.Event()


class Interfata:
    def __init__(self):
        super().__init__()

        self.thread1 = None

        """Mainframe"""
        self.root = tk.Tk()
        self.root.geometry('520x320')
        self.root.title('Flywheel GUI')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.vcmd = (self.root.register(self.validat), '%P')
        self.vcmd2 = (self.root.register(self.validat2), '%P')

        """Voltage, Current, Power Frame"""
        self.create_voltage_current_power_frame()

        """Motor_Control Frame"""
        self.create_motor_frame()

        """COM Port Frame"""
        self.create_com_port_frame()

        self.root.mainloop()

    def create_voltage_current_power_frame(self):
        self.voltage_frame = ttk.Frame(self.mainframe, padding="3")
        self.voltage_frame.grid(row=0, column=0, padx=3, pady=3, sticky='nw')

        """Label and Spinbox for Voltage"""
        self.label1 = ttk.Label(self.voltage_frame, text='Voltage', font=('Brass Mono', 10))
        self.label1.grid(row=0, column=0, padx=10, pady=5)
        self.voltaj = ttk.Spinbox(self.voltage_frame, from_=9, to=13.5, increment=0.1, validate='key',
                                  validatecommand=self.vcmd)
        self.voltaj.grid(row=1, column=0, padx=10, pady=10)

        """Label and Spinbox for Current"""
        self.label2 = ttk.Label(self.voltage_frame, text='Current', font=('Brass Mono', 10))
        self.label2.grid(row=2, column=0, padx=10, pady=5)
        self.amper = ttk.Spinbox(self.voltage_frame, from_=1, to=96, increment=5, validate='key',
                                 validatecommand=self.vcmd)
        self.amper.grid(row=3, column=0, padx=10, pady=10)


        """Buttons for the setup of the power supply and to stop it as well"""
        self.button = ttk.Button(self.voltage_frame, text='Set_PWS', command=self.start_thread)
        self.button.grid(row=6, column=0, padx=10, pady=10)

        self.button2 = ttk.Button(self.voltage_frame, text='Off_PWS', command=self.stop_thread)
        self.button2.grid(row=7, column=0, padx=10, pady=10)

        self.button4 = ttk.Button(self.voltage_frame, text='Off_On', command=self.Off_On)
        self.button4.grid(row=8, column=0, padx=10, pady=10)

    def create_motor_frame(self):
        self.motor_frame = ttk.Frame(self.mainframe, padding="5")
        self.motor_frame.grid(row=0, column=2, padx=3, pady=3, sticky='nw')

        """Label Torque"""
        self.label5 = ttk.Label(self.motor_frame, text='Torque (Nm)', font=('Brass Mono', 10))
        self.label5.grid(row=0, column=0, padx=10, pady=5)
        self.label7 = ttk.Label(self.motor_frame, text='Loops', font=('Brass Mono', 10))
        self.label7.grid(row=2, column=0, padx=10, pady=5)
        # self.label6 = ttk.Label(self.motor_frame, text='Negative Torque', font=('Brass Mono', 10))
        # self.label6.grid(row=2, column=0, padx=10, pady=5)

        """Motor Spinbox"""
        self.motor = ttk.Spinbox(self.motor_frame, from_=9, to=13.5, increment=0.01, validate='key',
                                validatecommand=self.vcmd)
        self.motor.grid(row=1, column=0, padx=10, pady=10)

        self.times = ttk.Spinbox(self.motor_frame, from_=9, to=13.5, increment=0.01, validate='key',
                                validatecommand=self.vcmd)
        self.times.grid(row=3, column=0, padx=10, pady=10)

        # self.motor2 = ttk.Spinbox(self.motor_frame, from_=-5000, to=-100, increment=100, validate='key',
        #                          validatecommand=self.vcmd)
        # self.motor2.grid(row=3, column=0, padx=10, pady=10)

        """Motor Button"""
        self.button3 = ttk.Button(self.motor_frame, text='Motor', command=self.Motor_ON)
        self.button3.grid(row=4, column=0, padx=10, pady=10)



    def create_com_port_frame(self):
        self.com_port_frame = ttk.Frame(self.mainframe, padding="3")
        self.com_port_frame.grid(row=0, column=1, padx=3, pady=3, sticky='nw')

        """Label and Combobox for selecting the right COM port"""
        self.label4 = ttk.Label(self.com_port_frame, text="Select a COM port:", font=('Brass Mono', 10))
        self.label4.grid(row=0, column=0, padx=10, pady=5)

        self.combo = ttk.Combobox(self.com_port_frame, validate='key', validatecommand=self.vcmd2)
        self.combo.grid(row=1, column=0, padx=10, pady=10)



        self.refresh_button = ttk.Button(self.com_port_frame, text="Refresh", command=self.refresh_ports)
        self.refresh_button.grid(row=2, column=0, padx=10, pady=10)

        self.refresh_ports()

    """ Validate key function """

    def validat(self, P):
        if P == "":
            return True  # Being able to delete the value
        try:
            float(P)
            return True  # if the value can be converted to float then we can accept it
        except ValueError:
            return False  # if not then the value won't be taken into consideration

    def validat2(self, P):
        return False  # Blocks any value

    """Setup of the power supply"""

    def Trimitere_Parametri(self):
        try:
            """"Create object from Arduino class"""
            if not hasattr(self, 'ard'):
                self.ard = AR.AR(port=self.combo.get())

            self.ard.voltage = self.voltaj.get()
            self.ard.current = self.amper.get()
            if self.ard.ok == 1:
                self.ard.timePython = float(self.times.get()) * 10.

            while not stop_event.is_set():
                self.ard.moment()
                stop_event.wait(0.1)  # Check every 0.1 seconds if stop_event is set
        except Exception as e:
            print(f"Error in Trimitere_Parametri: {e}")

    """Start a new thread for Trimitere_Parametri"""

    def start_thread(self):
        stop_event.clear()  # Clear the stop event before starting the thread
        self.thread1 = threading.Thread(target=self.Trimitere_Parametri)
        self.thread1.daemon = True  # Allow thread to exit when the main program exits
        self.thread1.start()

    def stop_thread(self):
        stop_event.set()  # Signal the thread to stop
        self.root.after(100, self.check_thread)
        self.ard.voltage = 0
        self.ard.current = 0

    def Off_On(self):
        self.stop_thread()
        sleep(3)
        self.start_thread()

    def check_thread(self):
        if self.thread1.is_alive():
            self.root.after(100, self.check_thread)
        else:
            print('Thread stopped')

    """Function for detecting the COM ports"""

    def refresh_ports(self):
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        self.combo['values'] = port_list
        if port_list:
            self.combo.current(0)

    def Motor_ON(self):
        #function to controll the motor 
        #due to confidential reasons I can't use mine
