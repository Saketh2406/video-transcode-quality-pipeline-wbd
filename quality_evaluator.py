import subprocess

def evaluate_quality(reference_path, test_path):
    try:
        cmd = [
            "ffmpeg", "-i", reference_path, "-i", test_path,
            "-lavfi", "[0:v][1:v]ssim;[0:v][1:v]psnr",
            "-f", "null", "-"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stderr  # contains SSIM & PSNR logs
    except Exception as e:
        return f"Error running quality evaluation: {e}"
