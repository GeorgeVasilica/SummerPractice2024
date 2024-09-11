from asammdf import MDF, Signal
import matplotlib.pyplot as plt
import numpy as np

def putere():
    # Read the MDF file
    mdf = MDF('ASAM_FILES/test_8_6.mf4')


    # Extract data from specific channels
    signal_A = mdf.get('ACT2p5.LADC_PhaseCurrents.VCurrent')
    signal_V = mdf.get('ACT.MkcMipDCLinkVoltage')

    # Cut the signal data from 30 seconds to the end
    cut_signal_A = signal_A.cut(start=20, stop=None)
    cut_signal_V = signal_V.cut(start=20, stop=None)

    # Interpolate voltage values to the timestamps of current
    interpolated_voltage = np.interp(cut_signal_A.timestamps, cut_signal_V.timestamps, cut_signal_V.samples)
    power_values = cut_signal_A.samples * interpolated_voltage

    # Calculate power values by multiplying current and interpolated voltage values
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 6))
    return Signal(samples=power_values, timestamps= cut_signal_A.timestamps, name='Power', unit='W')

    # Create subplots
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 6))
    # fig.suptitle('Prima incercare')

    # try:
    #     # # Plot the original current signal data in the first subplot
    #     # ax1.plot(signal_A.timestamps, signal_A.samples)
    #     # ax1.set_title('Original Current Signal')
    #     #
    #     # # Plot the original voltage signal data in the second subplot
    #     # ax2.plot(signal_V.timestamps, signal_V.samples, color='red')
    #     # ax2.set_title('Original Voltage Signal')
    #
    #     # Plot the power signal data in the third subplot
    #     # ax3.plot(cut_signal_A.timestamps, power_values, color='blue')
    #     # ax3.set_title('Power Signal (Current * Voltage)')
    #
    #     # Display the plots
    #     # plt.show()
    #
    # except KeyboardInterrupt:
    #     print("Program interrupted from keyboard")
    #
