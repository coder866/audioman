# audiomanipulator.py
from audio_functions import detect_media_type, cut_audio, trim_audio, convert_format, audio_to_mp4

def main():
    print("Welcome to AudioManipulator!")
    print("Please provide the following inputs:\n")

    # Prompt for inputs
    input_file = input("Input file (-i): ").strip()
    output_file = input("Output file (-o): ").strip()
    target_format = input("Target format (-f, optional): ").strip()
    start_time = input("Start time for cutting (-s, optional, hh:mm:ss): ").strip()
    end_time = input("End time for cutting (-e, optional, hh:mm:ss): ").strip()
    trim_duration = input("Trim duration (-t, optional, in seconds): ").strip()
    to_mp4 = input("Convert to MP4? (--to-mp4, yes/no): ").strip().lower() == "yes"
    image_file = input("Image file for MP4 conversion (--image, optional): ").strip() if to_mp4 else None

    # Detect media type
    try:
        media_type = detect_media_type(input_file)
        print(f"\nDetected media type: {media_type}")
    except ValueError as e:
        print(e)
        return

    # Construct the command based on inputs
    constructed_command = ["python", "audiomanipulator.py", "-i", input_file, "-o", output_file]
    if target_format:
        constructed_command.extend(["-f", target_format])
    if start_time and end_time:
        constructed_command.extend(["-s", start_time, "-e", end_time])
    if trim_duration:
        constructed_command.extend(["-t", trim_duration])
    if to_mp4:
        constructed_command.append("--to-mp4")
        if image_file:
            constructed_command.extend(["--image", image_file])

    # Print the constructed command
    print("\nConstructed command:", " ".join(constructed_command))

    # Perform operations based on inputs
    if start_time and end_time:
        cut_audio(input_file, output_file, start_time, end_time)
    elif trim_duration:
        trim_audio(input_file, output_file, trim_duration)
    elif to_mp4:
        if not image_file:
            print("Error: Image file is required for audio-to-MP4 conversion.")
            return
        audio_to_mp4(input_file, output_file, image_file)
    elif target_format:
        convert_format(input_file, output_file, target_format)
    else:
        print("Error: No operation specified.")

if __name__ == "__main__":
    main()