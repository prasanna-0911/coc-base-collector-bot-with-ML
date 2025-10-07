import subprocess
import time
import pyperclip
import csv
from datetime import datetime
import os
import torch
from PIL import Image

# ---------------------------
# Model setup
# ---------------------------
MODEL_PATH = os.path.join("..", "models", "best_windows.pt")  # relative path from src/
model = torch.hub.load('../yolov5', 'custom', path=MODEL_PATH, source='local', force_reload=False)

# ---------------------------
# Functions
# ---------------------------
def detect_base_coordinates(image_path, screen_width=1080, screen_height=2400):
    """
    Detect base coordinates using YOLOv5 model.
    Returns center x,y of the first detected object or None.
    """
    results = model(image_path)
    boxes = results.xyxy[0].cpu().numpy()  # x1, y1, x2, y2, conf, cls
    if len(boxes) == 0:
        print("❌ No base detected.")
        return None
    x1, y1, x2, y2, *_ = boxes[0]
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
    print(f"✅ Detected base at (center): ({center_x}, {center_y})")
    return center_x, center_y

def get_pc_clipboard(timeout=10):
    """Wait for new clipboard content containing a URL."""
    previous = pyperclip.paste()
    print("📋 Waiting for new clipboard content...")
    for _ in range(timeout * 2):
        current = pyperclip.paste()
        if current and current != previous and "https://" in current:
            print(f"✅ Link captured from clipboard: {current}")
            return current
        time.sleep(0.5)
    print("⚠️ No new clipboard content found.")
    return ""

def adb_tap(x, y):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
    print(f"📱 Tap at ({x}, {y})")

def adb_swipe(x1, y1, x2, y2, duration=300):
    subprocess.run(["adb", "shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration)])
    print(f"📱 Swipe from ({x1},{y1}) to ({x2},{y2})")

def adb_text(text):
    subprocess.run(["adb", "shell", "input", "text", text])
    print(f"⌨️ Input text: {text}")

def adb_keyevent(key_code):
    subprocess.run(["adb", "shell", "input", "keyevent", str(key_code)])

def adb_screenshot(filename):
    device_path = "/sdcard/screen_temp.png"
    subprocess.run(["adb", "shell", "screencap", "-p", device_path])
    subprocess.run(["adb", "pull", device_path, filename])
    subprocess.run(["adb", "shell", "rm", device_path])
    print(f"📸 Screenshot saved: {filename}")

# ---------------------------
# Main script
# ---------------------------
def main():
    CSV_FILENAME = os.path.join("..", "examples", "sample_output.csv")
    SCREENSHOT_FOLDER_COORDS = os.path.join("..", "Screenshots_Coords")
    SCREENSHOT_FOLDER_FINAL = os.path.join("..", "Screenshots_Final")
    
    os.makedirs(SCREENSHOT_FOLDER_COORDS, exist_ok=True)
    os.makedirs(SCREENSHOT_FOLDER_FINAL, exist_ok=True)
    
    num_bases = 2000  # You can modify this or add argparse later
    
    for i in range(num_bases):
        print(f"\n📲 Processing base {i+1}")

        # Tap middle button twice
        adb_tap(538, 2333)
        time.sleep(0.7)
        adb_tap(538, 2333)
        time.sleep(0.2)

        # Open the app (Clash Base Pedia)
        adb_tap(347, 1375)
        time.sleep(2)

        # Tap backward arrow
        adb_tap(75, 184)
        time.sleep(0.8)

        # Scroll down
        adb_swipe(541, 1321, 541, -100, duration=1200)
        time.sleep(0.1)

        # Take screenshot for detection
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(SCREENSHOT_FOLDER_COORDS, f"base_{timestamp}.png")
        adb_screenshot(screenshot_path)

        # Detect base
        result = detect_base_coordinates(screenshot_path)
        if result:
            base_x, base_y = result
            adb_tap(base_x, base_y)
            time.sleep(1.5)

        # Tap on base image for final screenshot
        adb_tap(538, 762)
        time.sleep(1.5)

        # Take final screenshot
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        final_filename = os.path.join(SCREENSHOT_FOLDER_FINAL, f"base_{timestamp}.png")
        adb_screenshot(final_filename)

        # Tap backward arrow
        adb_tap(77, 188)
        time.sleep(0.8)

        # Tap bookmark & copy base
        adb_tap(1016, 1116)
        time.sleep(0.1)
        adb_tap(193, 1139)
        time.sleep(2)

        # Tap address bar & copy
        adb_tap(453, 200)
        time.sleep(1.5)
        adb_tap(841, 361)
        time.sleep(0.5)

        # Get clipboard content
        base_url = pyperclip.paste()
        print(f"✅ Link pasted from clipboard: {base_url}")

        # Save to CSV
        with open(CSV_FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([final_filename, base_url])
            print(f"✅ Saved: {final_filename} → {base_url}")

if __name__ == "__main__":
    main()
