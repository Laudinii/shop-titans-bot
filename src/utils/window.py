import pygetwindow as gw

def get_game_window(title="Shop Titans"):
    windows = gw.getWindowsWithTitle(title)

    # ERROR
    if not windows:
        print("Game window not found!")
        return None
    
    # SUCCESS
    print("Game window found:", windows[0])
    return windows[0]

def get_game_region(window, ignore_titlebar=True):
    """Return (left, top, width, height). Optionally ignore Windows title bar (~30px)."""
    top = window.top + 30 if ignore_titlebar else window.top
    return (window.left, top, window.width, window.height)