# YouTube Media Downloader & Converter

A sleek and efficient Python-based tool that allows users to download YouTube videos in high quality and optionally convert them into MP3 audio format. This project demonstrates modular programming, file system management, and integration with third-party APIs.

## Features
- **High-Quality Downloads:** Automatically fetches the highest available resolution for MP4 files.
- **MP3 Conversion:** One-click conversion from video to audio format.
- **Modular Architecture:** Clean separation of concerns with `main.py` (CLI) and `utils.py` (Logic).
- **Error Handling:** Robust error management to handle invalid URLs or connection issues.
- **Clean Workspace:** Automatically manages download directories and file naming.

## Tech Stack
- **Language:** Python 3.14.2
- **Libraries:** - `pytubefix`: For interfacing with YouTube.
  - `moviepy` / `os`: For media processing and file management.

## Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/AtamertKoc/yt-mp3-converter.git](https://github.com/AtamertKoc/yt-mp3-converter.git)
   cd yt-mp3-converter
2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
3. **Run the Application:**
   ```bash
   python main.py
   Files will be downloaded directly to your system's Downloads folder.
