# 🎬 Video Transcoding & Quality Evaluation Pipeline

This project simulates a simplified media engineering workflow, inspired by Warner Bros. Discovery’s media supply chain.

---

## 🔧 Features
- Transcodes input videos into 1080p and 720p using FFmpeg
- Extracts video/audio metadata using `ffprobe`
- Compares video quality using **PSNR** and **SSIM** metrics
- Outputs structured reports in **JSON** and **TXT** formats

---

## 📂 Folder Structure

video-transcode-quality-pipeline-wbd/
├── input_videos/ # Place raw input video here (e.g., sample.mp4)
├── transcoded_videos/ # Output videos (1080p, 720p)
├── metadata_reports/ # JSON metadata per video
├── quality_reports/ # PSNR and SSIM logs
├── transcode.py # Handles FFmpeg video transcoding
├── metadata_extractor.py # Extracts metadata using ffprobe
├── quality_evaluator.py # Quality comparison logic
├── run_pipeline.py # Master runner script
├── requirements.txt # Optional: Python dependencies
└── README.md # This file


---

## 🛠️ Tools & Technologies

- Python 3.x
- FFmpeg (for transcoding and video quality analysis)
- ffprobe (for metadata extraction)
- Subprocess, JSON (standard Python libraries)

---

## 📦 Installation

1. **Install FFmpeg (includes `ffprobe`)**  
   - macOS:  
     ```bash
     brew install ffmpeg
     ```
   - Ubuntu:  
     ```bash
     sudo apt install ffmpeg
     ```
   - Windows: [FFmpeg for Windows](https://www.gyan.dev/ffmpeg/builds/)

2. **Clone the Repository**
   ```bash
   git clone https://github.com/Saketh2406/video-transcode-quality-pipeline-wbd.git
   cd video-transcode-quality-pipeline-wbd
