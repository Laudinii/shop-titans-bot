import pyautogui
import random
import time

def find_and_click(image_path, region=None, confidence=0.7):
    try:
        location = pyautogui.locateOnScreen(
            image_path, region=region, confidence=confidence
        )

        if location:
            center = pyautogui.center(location)
            x = center.x + random.randint(-5, 5)
            y = center.y + random.randint(-5, 5)
            pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.25))
            pyautogui.click()
            return True

    except pyautogui.ImageNotFoundException:
        return False

    return False

def collect_crafted_item(image_path, region=None, confidence=0.7):
    if (find_and_click(image_path, region, confidence)):
        print("Collected crafted item")
        time.sleep(1)
        print("Trying to confirm quality")
        if (find_and_click("images/collect-quality-confirm.png", region, 0.5)):
            print("Confirmed quality")
            time.sleep(0.1)
        else:
            print("No quality confirmation needed or couldn't find it")


def find_image(image_path, region=None, confidence=0.7):
    try:
        location = pyautogui.locateOnScreen(
            image_path, region=region, confidence=confidence
        )
        if location:
            return location
    except pyautogui.ImageNotFoundException:
        return None
    return None

def sell_item(image_path, region=None, confidence=0.7):
    if find_and_click(image_path, region, confidence):
        print("Sold item")
        time.sleep(0.3)
    else:
        print("Can't sell, try to refuse")
        if (find_and_click("images/sell-refuse.png", region, confidence)):
            print("Refused item")
            time.sleep(0.3)
