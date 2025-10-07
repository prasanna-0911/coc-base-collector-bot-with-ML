🧠 Clash of Clans Base Collector Bot

🚀 Overview
Clash of Clans Base Collector Bot is an AI-powered automation tool that collects Clash of Clans base layouts directly from your Android device.

It combines YOLOv5 object detection and ADB automation to:
- Detect base layouts from screenshots,
- Extract shareable base links,
- And save them automatically into a structured CSV file.

This project demonstrates skills in AI model deployment, computer vision, and automation engineering.


✨ Features
- 🧩 Detects base layouts using a custom-trained YOLOv5 model.  
- 🤖 Automates clicks, swipes, and text actions via ADB.  
- 🖼️ Captures screenshots and extracts shareable base links.  
- 📂 Saves output in clean CSV format for further use.  
- 💻 Works on Windows, Linux, and macOS.

🧱 Repository Structure
```
coc-base-collector-bot/
│── yolov5/ # Packaged YOLOv5 repo (minimal version)
│── models/
│ └── best_windows.pt # Trained model (14 MB)
│── examples/
│ ├── sample_output.csv # Example output file
│ └── workflow_diagram.png # Workflow diagram (this image)
│── src/
│ └── main.py # Main automation script
│── requirements.txt # Dependencies
│── LICENSE # MIT License
│── README.md # Project documentation
```

## ⚙️ Setup Instructions

1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/coc-base-collector-bot.git
cd coc-base-collector-bot

2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed.

pip install -r requirements.txt

3️⃣ Connect Android Device
1. Enable USB Debugging in Developer Options.

2. Connect your device via USB and authorize the computer.

3. Test connection:

```
adb devices
You should see your device ID listed.
```

4️⃣ Run the Bot
```
python src/main.py
```

🧩 How It Works
1. Screenshot Capture – The bot uses ADB to capture the current screen.

2. Base Detection – YOLOv5 model (best_windows.pt) identifies the base area.

3. Automated Interaction – The bot simulates touch inputs to open, copy, or navigate base links.

4. Result Logging – Extracted links and metadata are stored in sample_output.csv.


🧠 Model Information
1. Model: best_windows.pt (14 MB)

2. Framework: PyTorch YOLOv5

3. Dataset: Will be added later

4. Backup Link: (HuggingFace or Google Drive — To be added soon)

This model enables the bot to recognize base layouts visually and trigger the correct automation sequence.

💡 Future Enhancements
- Support for multiple base detection per screenshot.

- Include dataset and training scripts.

- Add GUI for one-click control.

- Introduce cloud upload for collected base data.

🧾 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for personal or commercial purposes.

🤝 Contributing
Pull requests are welcome!
If you’d like to improve detection accuracy, add new features, or integrate with Clash data APIs — feel free to fork and contribute.

🧑‍💻 Author
Developed by prasanna-0911
For showcasing skills in AI automation and computer vision engineering.

⭐ Support
If you like this project, consider giving it a ⭐ on GitHub — it really helps!

