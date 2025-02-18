# audio_functions.py
import subprocess
import filetype

def detect_media_type(file_path):
    """Detect the media type of the input file."""
    kind = filetype.guess(file_path)
    if kind is None:
        raise ValueError("Unsupported or unknown file format.")
    return kind.mime

def cut_audio(input_file, output_file, start, end):
    """Cut audio between start and end times."""
    command = [
        "ffmpeg", "-i", input_file, "-ss", start, "-to", end,
        "-c", "copy", output_file
    ]
    print("\nExecuting command:", " ".join(command))
    subprocess.run(command, check=True)

def trim_audio(input_file, output_file, duration):
    """Trim audio to a specific duration."""
    command = [
        "ffmpeg", "-i", input_file, "-t", duration,
        "-c", "copy", output_file
    ]
    print("\nExecuting command:", " ".join(command))
    subprocess.run(command, check=True)

def convert_format(input_file, output_file, target_format):
    """Convert audio to the target format."""
    command = [
        "ffmpeg", "-i", input_file, "-vn", "-acodec", "copy",
        output_file
    ]
    print("\nExecuting command:", " ".join(command))
    subprocess.run(command, check=True)

def audio_to_mp4(input_file, output_file, image_file):
    """Convert audio to MP4 with a static image."""
    command = [
        "ffmpeg", "-loop", "1", "-i", image_file, "-i", input_file,
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac",
        "-b:a", "192k", "-pix_fmt", "yuv420p", "-shortest", output_file
    ]
    print("\nExecuting command:", " ".join(command))
    subprocess.run(command, check=True)