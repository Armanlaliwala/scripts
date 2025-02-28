import os
import subprocess

# Define input and output folders
input_folder = "path/to/your/video/folder"  # Change this to your actual input folder
output_folder = "path/to/output/folder"  # Change this to your actual output folder
clip_duration = 5 * 60  # 5 minutes in seconds

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all video files in the input folder
video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

for video in video_files:
    input_path = os.path.join(input_folder, video)
    output_base = os.path.join(output_folder, os.path.splitext(video)[0])

    # FFmpeg command to split the video
    command = [
        "ffmpeg", "-i", input_path, "-c", "copy", "-map", "0", 
        "-segment_time", str(clip_duration), "-f", "segment", 
        "-reset_timestamps", "1", f"{output_base}_part%03d.mp4"
    ]
    
    subprocess.run(command)

print("Clipping completed! Videos are saved in the output folder.")
