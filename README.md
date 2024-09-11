# Flywheel Motor Control GUI

This project was developed as part of a Summer Practice program at Continental. It features a Python-based GUI to control a power supply feeding a motor that drives a flywheel. Upon receiving a certain torque request, the motor switches to generator mode, utilizing the flywheel's kinetic energy to generate power.

## Features

- **Power Supply Control:** The GUI uses multithreading to control the power supply, ensuring smooth operation.
- **COM Port Selector:** Easily select and connect to the correct COM port for communication.
- **Motor Control Panel:** A dedicated section on the right side of the GUI allows for motor control. However, due to confidentiality, specific motor control functions are not included.
- **Arduino NANO Integration:** The system uses an Arduino NANO to control the power supply and manage several relays that are activated or deactivated as needed.

## How It Works

1. **Power Supply Control:** The GUI communicates with an Arduino NANO to set the power supply parameters, allowing the motor to drive the flywheel.
2. **Motor Operation:** Upon a torque request, the motor switches to generator mode, using the flywheel's kinetic energy to generate power.
3. **Relay Control:** Relays are managed through the Arduino, turning them on and off according to the operational requirements.

## Requirements

- Python 3.x
- Arduino NANO
- Motor and Flywheel setup
- USB COM port connection

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git](https://github.com/GeorgeVasilica/SummerPractice_PowerSupply_Control_Arduino.git
