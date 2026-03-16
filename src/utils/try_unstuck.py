
import time
from utils import find_and_click

QUALITY_CONFIRM_IMG = "images/collect-quality-confirm.png"
QUALITY_CONFIRM_IMG_2 = "images/collect-quality-confirm2.png"
SELL_BUTTON_IMG = "images/sell-button.png"
SELL_REFUSE_IMG = "images/sell-refuse.png"

UNSTUCK_INTERVAL_SECONDS = 10
_last_unstuck_check = 0.0


def try_unstuck(region):
    global _last_unstuck_check

    now = time.monotonic()
    if now - _last_unstuck_check < UNSTUCK_INTERVAL_SECONDS:
        return

    _last_unstuck_check = now

    if find_and_click(QUALITY_CONFIRM_IMG, region, 0.5):
        print("Collect quality (1) cleanup")
        time.sleep(0.2)

    if find_and_click(QUALITY_CONFIRM_IMG_2, region, 0.5):
        print("Collect quality (2) cleanup")
        time.sleep(0.2)

    if find_and_click(SELL_BUTTON_IMG, region, 0.5):
        print("Sell cleanup")
        time.sleep(0.2)

    if find_and_click(SELL_REFUSE_IMG, region, 0.5):
        print("Sell refuse cleanup")
        time.sleep(0.2)

    print("Unstuck check complete")
