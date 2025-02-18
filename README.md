# AudioManipulator

**AudioManipulator** is a Python-based command-line tool for manipulating audio files. It allows you to cut, trim, convert, and transform audio files with ease. The tool uses `FFmpeg` under the hood for powerful audio processing.

---

## Features

- **Cut Audio**: Cut audio between specific start and end times.
- **Trim Audio**: Trim audio to a specific duration.
- **Convert Formats**: Convert audio files between formats (e.g., MP3, M4A, OGG, etc.).
- **Audio to MP4**: Convert audio files to MP4 with a static image.
- **Media Type Detection**: Automatically detect the input file format.

---

## Installation

### Prerequisites

1. **FFmpeg**: Ensure `FFmpeg` is installed on your system.
   - On Ubuntu/Debian:
     ```bash
     sudo apt install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - On Windows: Download from [FFmpeg's official website](https://ffmpeg.org/download.html).

2. **Python**: Ensure Python 3.6 or higher is installed.

### Install Dependencies

1. Clone the repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd audiomanipulator
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Arguments

- **Cut Audio**:
  ```bash
  python audiomanipulator.py cut --input input.mp3 --start 00:00:30 --end 00:01:00 --output output.mp3
  ```
- **Trim Audio**:
  ```bash
  python audiomanipulator.py trim --input input.mp3 --duration 60 --output output.mp3
  ```
- **Convert Formats**:
  ```bash
  python audiomanipulator.py convert --input input.mp3 --format ogg --output output.ogg
  ```
- **Audio to MP4**:
  ```bash
  python audiomanipulator.py audio_to_mp4 --input input.mp3 --image image.jpg --output output.mp4
  ```
- **Media Type Detection**:
  ```bash
  python audiomanipulator.py detect --input input.mp3
  ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.