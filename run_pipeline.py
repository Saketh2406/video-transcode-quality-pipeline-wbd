import os
import json
from transcode import transcode_video
from metadata_extractor import extract_metadata
from quality_evaluator import evaluate_quality

# Paths
INPUT_PATH = "input_videos/sample.mp4"
TRANSCODE_DIR = "transcoded_videos"
META_DIR = "metadata_reports"
QUALITY_DIR = "quality_reports"

# Create output folders if they don't exist
os.makedirs(META_DIR, exist_ok=True)
os.makedirs(QUALITY_DIR, exist_ok=True)

# Step 1: Transcode original to multiple resolutions
print("🔄 Starting Transcoding...")
transcode_video(INPUT_PATH, TRANSCODE_DIR)

# Step 2: Metadata for original
print("📝 Extracting metadata for original video...")
original_meta = extract_metadata(INPUT_PATH)
with open(os.path.join(META_DIR, "original.json"), "w") as f:
    json.dump(original_meta, f, indent=2)

# Step 3: Loop through each transcoded file
for file in os.listdir(TRANSCODE_DIR):
    trans_path = os.path.join(TRANSCODE_DIR, file)

    # Step 3a: Extract metadata
    print(f"📝 Extracting metadata for {file}...")
    meta = extract_metadata(trans_path)
    with open(os.path.join(META_DIR, f"{file}.json"), "w") as f:
        json.dump(meta, f, indent=2)

    # Step 3b: Evaluate video quality
    print(f"📊 Evaluating quality for {file}...")
    quality_log = evaluate_quality(INPUT_PATH, trans_path)
    with open(os.path.join(QUALITY_DIR, f"{file}_quality.txt"), "w") as f:
        f.write(quality_log)

print("\n✅ Pipeline completed.")
