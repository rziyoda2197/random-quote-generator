Men sizga 50 ta masalani hal qilish uchun kerakli kodni beraman.

### 1. Random Quote Generator with Categories
```python
import random

quotes = {
    "motivatsiya": [
        "Menimcha, hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Menimcha, hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
    ],
    "hayot": [
        "Hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Menimcha, hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
    ],
    "hazil": [
        "Menimcha, hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
        "Menimcha, hayotda muvaffaqiyatga erishish uchun birinchi shart – oʻzingizga ishonish.",
    ],
}

def get_quote(category):
    return random.choice(quotes[category])

def save_daily_quote():
    with open("daily_quote.txt", "w") as f:
        f.write(get_quote("motivatsiya"))

save_daily_quote()
```

### 2. News Headline Scraper Simulator
```python
import random

news_headlines = [
    "COVID-19: Jahon salomatlik tashkiloti COVID-19 pandemiyasi haqida yangiliklar berdi.",
    "Rossiya-Ukraina urushi: Rossiya-Ukraina urushi haqida yangiliklar berdi.",
    "COVID-19: Jahon salomatlik tashkiloti COVID-19 pandemiyasi haqida yangiliklar berdi.",
    "Rossiya-Ukraina urushi: Rossiya-Ukraina urushi haqida yangiliklar berdi.",
    "COVID-19: Jahon salomatlik tashkiloti COVID-19 pandemiyasi haqida yangiliklar berdi.",
]

def search_news(keyword):
    return [headline for headline in news_headlines if keyword in headline]

def print_news(headlines):
    for headline in headlines:
        print(headline)

keyword = input("Kalit so'zni kiriting: ")
headlines = search_news(keyword)
print_news(headlines)
```

### 3. Simple RSS Feed Reader
```python
import feedparser

rss_feeds = [
    "https://www.bbc.co.uk/news/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.cnn.com/services/rss/rss.xml",
]

def read_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)
    return feed.entries

def print_feed(entries):
    for entry in entries:
        print(entry.title)
        print(entry.link)
        print(entry.description)
        print()

feed_url = rss_feeds[0]
entries = read_rss_feed(feed_url)
print_feed(entries)
```

### 4. PDF Metadata Extractor
```python
import PyPDF2

def extract_metadata(file_path):
    pdf_file = open(file_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = {}
    metadata["title"] = pdf_reader.metadata.title
    metadata["author"] = pdf_reader.metadata.author
    metadata["created"] = pdf_reader.metadata.created
    metadata["modified"] = pdf_reader.metadata.modified
    metadata["page_count"] = len(pdf_reader.pages)
    return metadata

file_path = "example.pdf"
metadata = extract_metadata(file_path)
print(metadata)
```

### 5. Image Batch Resizer
```python
from PIL import Image

def resize_images(directory, output_directory, width, height):
    import os
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            image = image.resize((width, height))
            output_path = os.path.join(output_directory, filename)
            image.save(output_path)

directory = "input"
output_directory = "output"
width = 800
height = 600
resize_images(directory, output_directory, width, height)
```

### 6. Audio File Metadata Reader
```python
import eyed3

def read_audio_metadata(file_path):
    audio_file = eyed3.load(file_path)
    metadata = {}
    metadata["artist"] = audio_file.tag.artist
    metadata["album"] = audio_file.tag.album
    metadata["title"] = audio_file.tag.title
    metadata["duration"] = audio_file.info.time_secs
    return metadata

file_path = "example.mp3"
metadata = read_audio_metadata(file_path)
print(metadata)
```

### 7. Video Duration Calculator
```python
import os

def calculate_video_duration(directory):
    total_duration = 0
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".avi"):
            file_path = os.path.join(directory, filename)
            video_file = open(file_path, "rb")
            video_duration = os.path.getsize(file_path) / 1024 / 1024 / 60
            total_duration += video_duration
    return total_duration

directory = "input"
total_duration = calculate_video_duration(directory)
print(total_duration)
```

### 8. Bulk File Renamer
```python
import os

def rename_files(directory, pattern):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            new_filename = pattern.replace("{}", filename.split(".")[0])
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)

directory = "input"
pattern = "vacation_{}.jpg"
rename_files(directory, pattern)
```

### 9. Folder Size Analyzer
```python
import os

def calculate_folder_size(directory):
    total_size = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            total_size += os.path.getsize(file_path)
        elif os.path.isdir(file_path):
            total_size += calculate_folder_size(file_path)
    return total_size

directory = "input"
total_size = calculate_folder_size(directory)
print(total_size)
```

### 10. Duplicate File Finder
```python
import os
import hashlib

def find_duplicate_files(directory):
    file_hashes = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
            if file_hash in file_hashes:
                file_hashes[file_hash].append(filename)
            else:
                file_hashes[file_hash] = [filename]
    return file_hashes

directory = "input"
file_hashes = find_duplicate_files(directory)
for file_hash, filenames in file_hashes.items():
    if len(filenames) > 1:
        print(f"Duplicate files: {filenames}")
```

### 11. Screenshot Taker with Timestamp
```python
import datetime
import pyautogui

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = f"screenshot_{timestamp}.png"
    pyautogui.screenshot().save(screenshot_path)

take_screenshot()
```

### 12. Clipboard Monitor
```python
import pyperclip

def monitor_clipboard():
    while True:
        clipboard_text = pyperclip.paste()
        print(clipboard_text)
        # Save clipboard text to file
        with open("clipboard.txt", "a") as f:
            f.write(clipboard_text + "\n")

monitor_clipboard()
```

### 13. Keyboard Activity Logger
```python
import pynput

def on_press(key):
    print(f"Key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")

listener = pynput.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
```

### 14. Mouse Movement Tracker
```python
import pyautogui

def track_mouse_movement():
    while True:
        position = pyautogui.position()
        print(f"Mouse position: {position}")
        # Save mouse position to file
        with open("mouse_position.txt", "a") as f:
            f.write(f"{position}\n")

track_mouse_movement()
```

### 15. System Information Dashboard
```python
import psutil

def get_system_info():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    battery_percent = psutil.sensors_battery().percent
    return {
        "
