# Real-Time Invisibility Cloak using Python & OpenCV

Bring the magic of Harry Potter to life! 🧙‍♂️  
This project uses computer vision to create a real-time invisibility cloak effect using Python, OpenCV, and NumPy.

## Features

- 🎨 Color-based cloak detection (auto-selected or manually drawn)
- 🖌️ Manual mask drawing support
- 🔄 Dynamic mask blending
- 🧠 Combines automatic and manual masking
- ⚡ Real-time performance

## 📸 Demo

![demo](demo.gif)

## 🧠 How it Works

1. Capture a static background.
2. Detect a selected cloak color or user-drawn region.
3. Replace the detected region with the background — making it invisible!

## 🧪 Technologies Used

- Python 🐍
- OpenCV 🎥
- NumPy 🔢

## 🛠️ Installation

```bash
git clone https://github.com/your-username/invisibility-cloak.git
cd invisibility-cloak
pip install -r requirements.txt
python invisibility_cloak.py
🎮 Controls
Ctrl + Click → Pick cloak color

Draw with mouse → Manually mark cloak

Press c → Clear drawing

Press q → Quit

✅ Requirements
Python 3.7+

txt
Copy
Edit
opencv-python
numpy
🧠 Ideas for Future Enhancements
Gesture control using MediaPipe

GUI with sliders for HSV ranges

Background video replacement

Multi-color support

Save snapshots or record video

📄 License
MIT License
