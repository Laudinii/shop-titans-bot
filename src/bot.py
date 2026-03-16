from utils import get_game_window, get_game_region, start_selling, start_collecting, try_unstuck
import time

def run_crafting_placeholder(region):
    print("Crafting routine placeholder")
    return False

def main():
    print("Bot starting...")
    window = get_game_window()
    if not window:
        return

    region = get_game_region(window)

    while True:
        start_selling(region)
        start_collecting(region)
        # run_crafting_placeholder(region)

        try_unstuck(region)

        time.sleep(0.2)

if __name__ == "__main__":
    main()