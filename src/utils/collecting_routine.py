
import time
from utils import collect_crafted_item, find_image

COLLECT_READY_IMG = "images/collect-ready-button.png"


def start_collecting(region):
    # "READY" icon

    while (find_image(COLLECT_READY_IMG, region, 0.7)):
        if collect_crafted_item(COLLECT_READY_IMG, region, 0.7):
            print("Collect ready")
            time.sleep(0.05)
