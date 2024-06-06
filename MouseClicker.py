import pyautogui
import time
import threading
import sys

# Function to click at the current mouse position
def click_mouse():
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(10)  # Wait for 10 seconds before clicking again

# Function to listen for a key press to stop the script
def stop_script():
    input("Press Enter to stop the script...\n")
    stop_event.set()
    sys.exit()

# Event to stop the thread
stop_event = threading.Event()

# Start the mouse clicker thread
click_thread = threading.Thread(target=click_mouse)
click_thread.start()

# Start the stop script listener
stop_script()
