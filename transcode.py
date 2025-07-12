import subprocess
import os

def transcode_video(input_path, output_dir):
    # Define target resolutions
    resolutions = {
        "1080p": "1920x1080",
        "720p": "1280x720"
    }

    # Extract base name without extension
    base = os.path.splitext(os.path.basename(input_path))[0]
    os.makedirs(output_dir, exist_ok=True)

    # Loop over each resolution and transcode
    for label, res in resolutions.items():
        output_path = os.path.join(output_dir, f"{base}_{label}.mp4")
        print(f"Transcoding to {label} → {output_path}")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-vf", f"scale={res}",
            "-c:v", "libx264", "-crf", "23", "-preset", "fast",
            "-c:a", "copy",
            output_path
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
