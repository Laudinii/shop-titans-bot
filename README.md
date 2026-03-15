# Shop Titans Automation Bot

A simple automation bot for **Shop Titans** that uses screen recognition to detect UI elements and perform actions like crafting, collecting, and selling items.

This project is intended as a **learning project for automation and computer vision**, demonstrating how to interact with a game window using image recognition and simulated mouse input.

---

## Overview

The bot works by:

1. Capturing screenshots of the screen.
2. Detecting UI elements (buttons, icons) using image matching.
3. Moving the mouse and clicking on detected elements.
4. Repeating the process in a loop.

It uses:

- **Python**
- **OpenCV** for image detection
- **PyAutoGUI** for mouse/keyboard automation

---

## Features

- Detects UI buttons via image recognition
- Automatically clicks crafting and collection buttons
- Simple architecture that is easy to expand
- Local virtual environment support

---

## Requirements

Install:

- Python 3.9+
- pip

Python libraries:

- pyautogui
- pygetwindow
- opencv-python
- numpy
- pillow

All dependencies are listed in `requirements.txt`.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/shop-titans-bot.git
cd shop-titans-bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
shop-titans-bot
│
├── src/
│   └── bot.py
│
├── images/
│   ├── craft.png
│   ├── collect.png
│   └── sell.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Preparing Image Templates

The bot relies on **template images** of UI elements.

Create screenshots for buttons such as:

- Craft button
- Collect button
- Sell button

Guidelines:

- Use PNG format
- Crop tightly around the UI element
- Avoid background elements
- Ensure the game resolution remains constant

Place the images inside the `images/` directory.

---

## Running the Bot

Start the game and make sure it is:

- Running in **windowed mode**
- Using a **fixed resolution**
- Not moved after starting the bot

Run the script:

```bash
python src/bot.py
```

The bot will continuously scan the screen and click detected buttons.

---

## Safety Stop

Move the mouse to the **top-left corner of the screen** to trigger PyAutoGUI's fail-safe and stop the bot.

---

## Customization

Possible improvements include:

- Limiting scanning to the game window
- Adding randomized mouse movements
- Supporting multiple crafting slots
- OCR-based number reading
- State-machine logic for smarter automation

---

## Disclaimer

This project is for **educational purposes only**.

Automation may violate the terms of service of some games. Use responsibly and at your own risk.

The author is not responsible for any account restrictions or bans resulting from the use of this software.

---

## License

MIT License
