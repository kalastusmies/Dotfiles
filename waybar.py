import psutil
import subprocess
import time
import logging

logging.basicConfig(filename='/tmp/waybar_start.log', level=logging.INFO)

def check_and_run_waybar():
    logging.info("Checking if Waybar is running...")
    # Check if 'waybar' is already running
    for proc in psutil.process_iter(['pid', 'name']):
        if 'waybar' in proc.info['name'].lower():
            logging.info("Waybar is already running.")
            return True  # 'waybar' is running, return True

    # If 'waybar' is not running, start it
    logging.info("Waybar is not running. Starting it now...")
    subprocess.Popen(['waybar'])
    return False  # 'waybar' was not running and is now being started

# Delay to allow the graphical environment to be ready
time.sleep(10)  # Adjust this value as needed

# Call the function and check if 'waybar' is running
while True:
    check_and_run_waybar()
    time.sleep(60)  # Check every 60 seconds if Waybar is running
