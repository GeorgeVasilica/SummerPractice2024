import shutil
from asammdf import MDF
import matplotlib.pyplot as plt
import os


class ASAM:
    def __init__(self, **kwargs):
        # Read the MDF file
        self.static_c = 0
        self.mdf = MDF(kwargs['MDF_FILE'])

    def extract_signal(self, signal_name):
        try:
            signal = self.mdf.get(signal_name)
            return signal
        except KeyError:
            print(f"Signal {signal_name} not found in the MDF file.")
            return None

    def ploting(self, file):
        # Extract data from specific channels
        semnal = self.mdf.get(file)
        semnal.plot()

    def delete_file(self, directory_path):
        if os.path.exists(directory_path):
            # Iterate over all the files and directories in the directory
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                try:
                    # Check if it's a file or directory and remove accordingly
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Remove file or link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Remove directory and its contents
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')

    def sub_plot(self, val, **kwargs):
        if val == 1:
            self.ploting(kwargs['file'])
            return
        else:
            if val % 2 != 0:
                print('Val trb sa fie numar impar')
                return

        a = int(val / 2)  # Determine the grid size
        fig, axs = plt.subplots(a, a, figsize=(12, 12))

        # Initialize the signals list as a 2D list
        signals = [[None for _ in range(a)] for _ in range(a)]

        # Choose which measurements you want to see
        b = 1
        for i in range(a):
            for j in range(a):
                if f'file{b}' in kwargs:
                    signals[i][j] = self.mdf.get(kwargs[f'file{b}'])
                b += 1

        # Put on a graph every signal we want to see
        for i in range(a):
            for j in range(a):
                if signals[i][j]:
                    axs[i, j].plot(signals[i][j].timestamps, signals[i][j].samples)
                    axs[i, j].set_title(f'Subplot {i + 1},{j + 1}')
        directory = 'Plot_image/'
        os.makedirs(directory, exist_ok=True)  # Ensure the directory exists

        # Verify if the Image(number) already exists, if it does then go to the next number and create that Image
        while True:
            file_path = os.path.join(directory, f'Image{self.static_c}.png')
            if not os.path.exists(file_path):
                plt.savefig(file_path)
                break
            self.static_c += 1

        self.static_c += 1

    # plt.tight_layout()
    # plt.show()
