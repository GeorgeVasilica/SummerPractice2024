import os
import ASAM as AS
import ASAM2 as AS2
from asammdf import MDF


def DAXil():
    origin_directory = 'ASAM_FILES/'

    try:
        # Go through every mf4 file in the directory
        for file in os.listdir(origin_directory):
            filename = os.fsdecode(file)
            if filename.lower().endswith(".mf4"):
                # Set up the new MDF file path with "Generator" added to the original filename
                new_mdf_path = os.path.join(origin_directory, f"{os.path.splitext(filename)[0]}_Generator.mf4")

                # If the file already exists, remove it
                if os.path.exists(new_mdf_path):
                    os.remove(new_mdf_path)

                # Create a new MDF object
                new_mdf = MDF()

                # Load the ASAM file and extract signals
                asm = AS.ASAM(MDF_FILE=os.path.join(origin_directory, filename))

                signal = asm.extract_signal('ACT2p5.LADC_PhaseCurrents.VCurrent')
                signal2 = asm.extract_signal('ACT.MkcMipDCLinkVoltage')
                signal3 = AS2.putere()

                # signal4 = asm.extract_signal('ACT2p5.LADC_MDCC_DCCurrent.DCcurrent')
                # signal5 = asm.extract_signal('ACT2p5.LADC_MTC_ElectricalTorque.Torque')
                # signal6 = asm.extract_signal('ACT.MkcMipCalcMechSpeed')
                # signal7 = asm.extract_signal('ACT.MkcMipCalcMechSpeedFilt')
                t = 19
                p = 45
                if signal:
                    # Cut signals and append to the new MDF object
                    cut_signal = signal.cut(start=t, stop=p)
                    cut_signal2 = signal2.cut(start=t, stop=p)
                    cut_signal3 = signal3.cut(start=t, stop=p)
                    # cut_signal4 = signal4.cut(start=t, stop=p)
                    # cut_signal5 = signal5.cut(start=t, stop=p)
                    # cut_signal6 = signal6.cut(start=t, stop=p)
                    # cut_signal7 = signal7.cut(start=t, stop=p)

                    new_mdf.append(cut_signal)
                    new_mdf.append(cut_signal2)
                    new_mdf.append(cut_signal3)
                    # new_mdf.append(cut_signal4)
                    # new_mdf.append(cut_signal5)
                    # new_mdf.append(cut_signal6)
                    # new_mdf.append(cut_signal7)

                    # Save the new MDF file
                    new_mdf.save(new_mdf_path)
                    print(f"New MDF file saved at {new_mdf_path}")
                else:
                    print(f"No signal extracted for {filename}, skipping.")
    except KeyboardInterrupt:
        print("Program interrupted from keyboard")