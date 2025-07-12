# 🎬 Video Transcoding & Quality Evaluation Pipeline

This project simulates a simplified media engineering workflow, inspired by Warner Bros. Discovery’s media supply chain.

## 🔧 Features
- Transcode input videos into 1080p and 720p using FFmpeg
- Extract video/audio metadata using ffprobe
- Compare video quality using PSNR and SSIM metrics
- Output structured reports (JSON + TXT)

## 📂 Folder Structure
- `input_videos/`: Place your original video here
- `transcoded_videos/`: Transcoded outputs
- `metadata_reports/`: Metadata files (.json)
- `quality_reports/`: Quality comparison logs (.txt)

## 🚀 Run the Pipeline
```bash
python run_pipeline.py
