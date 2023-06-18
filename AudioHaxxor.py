import os
import threading
from shutil import which
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pydub import AudioSegment

def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None

class AudioConverter:
    def __init__(self, root):
        self.root = root
        self.root.title('Audio H4xx0r')
        self.root.geometry('600x400')
        self.output_format = tk.StringVar()
        self.output_format.set('wav')  # default format
        self.folder_selected = 'Select Input Folder'
        self.thread = None
        self.create_widgets()
        self.check_dependencies()

    def create_widgets(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Select Folder', command=self.select_folder)

        formatmenu = tk.Menu(menu)
        menu.add_cascade(label='Format', menu=formatmenu)
        formatmenu.add_radiobutton(label='WAV', variable=self.output_format, value='wav')
        formatmenu.add_radiobutton(label='MP3', variable=self.output_format, value='mp3')

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='Help', command=self.show_help)
        helpmenu.add_command(label='About', command=self.show_about)

        self.label = tk.Label(self.root, text=self.folder_selected)
        self.label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text='Start Encoding', command=self.start_encoding)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text='Stop Encoding', command=self.stop_encoding, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1)

        self.terminal = scrolledtext.ScrolledText(self.root)
        self.terminal.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        self.label.config(text=self.folder_selected)

    def start_encoding(self):
        if self.folder_selected == 'Select Input Folder':
            messagebox.showwarning('No Folder Selected', 'Please select a folder first.')
            return

        self.thread = threading.Thread(target=self.convert_audio, args=(self.folder_selected,))
        self.thread.start()

        self.start_button['state'] = tk.DISABLED
        self.stop_button['state'] = tk.NORMAL

    def stop_encoding(self):
        if self.thread:
            self.thread = None

        self.start_button['state'] = tk.NORMAL
        self.stop_button['state'] = tk.DISABLED

    def convert_audio(self, folder):
        output_folder = os.path.join(folder, 'Converted')
        os.makedirs(output_folder, exist_ok=True)

        for file in os.listdir(folder):
            if not self.thread:
                break

                if file.endswith('.m4a'):
                    audio = AudioSegment.from_file(os.path.join(folder, file), format='m4a')
                    file_without_ext = os.path.splitext(file)[0]
                    audio.export(os.path.join(output_folder, file_without_ext + '.' + self.output_format.get()), format=self.output_format.get())
                    self.terminal.insert(tk.END, f'Converted {file} to {self.output_format.get()}\n')
                    self.terminal.see(tk.END)

    def check_dependencies(self):
        dependencies = ['ffmpeg']
        if self.output_format.get() == 'mp3':
            dependencies.append('lame')

        missing_dependencies = [dep for dep in dependencies if not is_tool(dep)]

        if missing_dependencies:
            missing_deps_str = ', '.join(missing_dependencies)
            messagebox.showerror("Missing dependencies", f"The following dependencies are missing: {missing_deps_str}")

    def show_help(self):
        messagebox.showinfo("Help", "This is a simple audio converter. First, select the folder containing the .m4a files "
                                    "you want to convert.\n\n Then, select the output format (WAV or MP3) from the 'Format' "
                                    "menu.\n\n Finally, click 'Start Encoding' to begin the conversion.\n\n The converted files "
                                    "will be saved in a subfolder named 'Converted' in the same directory as the input files.")

    def show_about(self):
        messagebox.showinfo("About", "Audio H4xx0r\n\nVersion 0.4.20. \n\nCreated by kFuQ.")

if __name__ == '__main__':
    root = tk.Tk()
    app = AudioConverter(root)
    root.mainloop()
