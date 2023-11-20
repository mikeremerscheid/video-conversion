

import subprocess
import os

from tkinter import Tk, filedialog


def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window

    folder_selected = filedialog.askdirectory(title="Select a Folder")
    return folder_selected


def convert_mkv_to_mp4(selected_folder):
    for filename in os.listdir(selected_folder):
        if filename.endswith(".mkv"):
            filepath = os.path.join(selected_folder, filename)
            subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    filepath,
                    "-c",
                    "copy",
                    "-movflags",
                    "+faststart",
                    filepath.replace(".mkv", ".mp4"),
                ]
            )
            os.remove(filepath)


if __name__ == "__main__":
    selected_folder = select_folder()

    if selected_folder:
        convert_mkv_to_mp4(selected_folder)
    else:
        print("No folder selected. Exiting.")
