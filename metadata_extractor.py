import subprocess
import json

def extract_metadata(video_path):
    try:
        cmd = [
            "ffprobe", "-v", "error",
            "-print_format", "json",
            "-show_format", "-show_streams",
            video_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        metadata = json.loads(result.stdout)
        return metadata
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return {}
