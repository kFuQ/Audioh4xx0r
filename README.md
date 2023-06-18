# Audio H4xx0r

Audio H4xx0r is a simple audio converter application. It is written in Python and provides a graphical user interface for the conversion of `.m4a` audio files to either `.wav` or `.mp3` format.

## Features

- Select a folder containing `.m4a` files to convert.
- Choose the output format (WAV or MP3) from the Format menu.
- Start and stop the conversion process with dedicated buttons.
- View the conversion progress in a terminal window within the application.
- All converted files are saved in a subfolder named 'Converted' in the same directory as the input files.

## Dependencies

- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- tkinter: Comes pre-installed with Python 3. [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- PyDub: [https://pypi.org/project/pydub/](https://pypi.org/project/pydub/)
- FFmpeg: [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html)
- LAME (for MP3 output): [http://lame.sourceforge.net/](http://lame.sourceforge.net/)

Please note that FFmpeg and LAME need to be installed and added to your PATH. 

## Installation

1. Install Python 3 and make sure that it is added to your PATH.
2. Install PyDub using pip:
    ```
    pip install pydub
    ```
3. Install FFmpeg and LAME and add them to your PATH.

## Usage

Run the `audio_converter.py` script to start the application:

