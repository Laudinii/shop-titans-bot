from utils import find_and_click, sell_item
import time

from utils.actions import find_image

SELL_BRANCH_IMG = "images/autosell-branch.png"
SELL_SHIV_IMG = "images/autosell-shiv.png"

SELL_IMG = "images/sell-button.png"


def sell_until_no_more(region, confidence=0.7):
    while find_image(SELL_IMG, region, confidence):
        print("Found more items to sell after initial sell")
        sell_item(SELL_IMG, region)
        time.sleep(0.2)


def start_selling(region):
    # BRANCH
    if find_and_click(SELL_BRANCH_IMG, region, 0.7):
        print("Found item to sell")
        time.sleep(0.2)
        sell_item(SELL_IMG, region)
        time.sleep(0.2)

    sell_until_no_more(region, 0.7)

    # SHIV
    if find_and_click(SELL_SHIV_IMG, region, 0.7):
        print("Found item to sell")
        time.sleep(0.2)
        sell_item(SELL_IMG, region)
        time.sleep(0.2)
        
    sell_until_no_more(region, 0.7)

    return False