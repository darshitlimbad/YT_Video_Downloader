# YouTube Video Downloader 2.0

Effortlessly download YouTube videos in the highest quality with our user-friendly YouTube Video Downloader. Whether you need the video, audio, or both, our tool handles it all, directly saving files to your chosen folder for easy access and convenience.

## Important Note

**Users should have downloaded FFmpeg on their PC because `yt_dlp` needs it to function properly.**

### How to Install FFmpeg

1. Download FFmpeg from the official website: [FFmpeg.org](https://ffmpeg.org/download.html).
2. Follow the installation instructions for your operating system.
3. Make sure FFmpeg is added to your system's PATH.

## Features

- Download videos in the highest quality.
- Option to download only audio or video.
- Save files directly to your specified folder.

## Requirements

- Python 3.6 or higher
- `yt_dlp` module
- FFmpeg (ensure it is installed and available in your system's PATH)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/darshitlimbad/YT_Video_Downloader.git
    ```
2. Navigate to the project directory:
    ```bash
    cd YT_Video_Downloader
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to download your desired video.

## Building the Executable

To build the executable file using cxfreeze, follow these steps:

1. Install cxfreeze:
    ```bash
    pip install cxfreeze
    ```
2. Generate the executable:
    ```bash
    cxfreeze main.py --build_exe dist/ --icon app.ico
    ```

The executable will be available in the `dist` folder.

## License

IDK