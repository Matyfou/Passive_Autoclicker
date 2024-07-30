import subprocess
import pickle
from pynput import mouse
import time
import threading
import os

# Launch menu.py as a separate process
menu_process = subprocess.Popen(['python', 'menu.py'])

# Global variables for left clicks
leftCpsToStart = 3
leftCpsToStop = 2
leftCpsTimeCheck = 0.1
leftClicksCount = 1
leftMaxTimeBetweenClicks = 0.4
leftEnabled = True

# Global variables for right clicks
rightCpsToStart = 3
rightCpsToStop = 2
rightCpsTimeCheck = 0.1
rightClicksCount = 1
rightMaxTimeBetweenClicks = 0.4
rightEnabled = True

# Global variables for click management
click_times = {'left': [], 'right': []}
last_user_click_time = {'left': None, 'right': None}
action_triggered = {'left': False, 'right': False}
simulated_click = {'left': False, 'right': False}
time_between_clicks = {'left': 1, 'right': 1}

# Mouse controller
mouse_controller = mouse.Controller()

# Lock to protect access to the configuration file
config_lock = threading.Lock()

# Function to load settings from the configuration file
def load_config():
    global leftCpsToStart, leftCpsToStop, leftCpsTimeCheck, leftClicksCount, leftMaxTimeBetweenClicks, leftEnabled
    global rightCpsToStart, rightCpsToStop, rightCpsTimeCheck, rightClicksCount, rightMaxTimeBetweenClicks, rightEnabled

    try:
        with config_lock:
            with open('config.pkl', 'rb') as f:
                config = pickle.load(f)
                # Left click
                leftCpsToStart = config["leftCpsToStart"]
                leftCpsToStop = config["leftCpsToStop"]
                leftCpsTimeCheck = config["leftCpsTimeCheck"]
                leftClicksCount = config["leftClicksCount"]
                leftMaxTimeBetweenClicks = config["leftMaxTimeBetweenClicks"]
                leftEnabled = config["leftEnabled"]
                # Right click
                rightCpsToStart = config["rightCpsToStart"]
                rightCpsToStop = config["rightCpsToStop"]
                rightCpsTimeCheck = config["rightCpsTimeCheck"]
                rightClicksCount = config["rightClicksCount"]
                rightMaxTimeBetweenClicks = config["rightMaxTimeBetweenClicks"]
                rightEnabled = config["rightEnabled"]
    except (FileNotFoundError, EOFError):
        pass


# Function to check CPS for left and right clicks
def check_cps():
    global action_triggered, click_times
    while True:
        load_config()  # Load configuration on each cycle

        # Checking CPS for left click
        if not leftEnabled:
            action_triggered['left'] = False
        else:
            current_time = time.time()
            click_times['left'][:] = [t for t in click_times['left'] if current_time - t <= 1]
            cps_left = len(click_times['left'])
            if cps_left > leftCpsToStart and not action_triggered['left']:
                action_triggered['left'] = True
                print("Left click action triggered!")
            elif cps_left < leftCpsToStop and action_triggered['left']:
                action_triggered['left'] = False
                print("Left click action stopped!")

        # Checking CPS for right click
        if not rightEnabled:
            action_triggered['right'] = False
        else:
            current_time = time.time()
            click_times['right'][:] = [t for t in click_times['right'] if current_time - t <= 1]
            cps_right = len(click_times['right'])
            if cps_right > rightCpsToStart and not action_triggered['right']:
                action_triggered['right'] = True
                print("Right click action triggered!")
            elif cps_right < rightCpsToStop and action_triggered['right']:
                action_triggered['right'] = False
                print("Right click action stopped!")

        time.sleep(leftCpsTimeCheck)  # Check CPS at the defined interval

# Function to check if menu.py is still running
def monitor_menu():
    while True:
        if menu_process.poll() is not None:
            print("menu.py has terminated. Shutting down main.py")
            os._exit(0)  # Terminate the main process
        time.sleep(1)  # Check every second

# Function called when a mouse button is clicked
def on_click(x, y, button, pressed):
    global simulated_click, last_user_click_time, time_between_clicks, leftEnabled, rightEnabled

    if button == mouse.Button.left and pressed and leftEnabled:
        if not simulated_click['left']:
            current_time = time.time()

            # Calculate the time between two user clicks
            if last_user_click_time['left'] is not None:
                time_between_clicks['left'] = current_time - last_user_click_time['left']

            last_user_click_time['left'] = current_time  # Update the last user click time
            click_times['left'].append(current_time)

            if action_triggered['left']:
                # Trigger an automatic left click after 100 ms
                threading.Thread(target=delayed_click, args=('left',)).start()

    elif button == mouse.Button.right and pressed and rightEnabled:
        if not simulated_click['right']:
            current_time = time.time()

            # Calculate the time between two user clicks
            if last_user_click_time['right'] is not None:
                time_between_clicks['right'] = current_time - last_user_click_time['right']

            last_user_click_time['right'] = current_time  # Update the last user click time
            click_times['right'].append(current_time)

            if action_triggered['right']:
                # Trigger an automatic right click after 100 ms
                threading.Thread(target=delayed_click, args=('right',)).start()

# Function to perform an automatic click after a delay
def delayed_click(button_type):
    global simulated_click, leftClicksCount, leftMaxTimeBetweenClicks, rightClicksCount, rightMaxTimeBetweenClicks
    if button_type == 'left':
        if time_between_clicks['left'] < leftMaxTimeBetweenClicks:
            for i in range(leftClicksCount):
                time.sleep(time_between_clicks['left'] / leftClicksCount)
                simulated_click['left'] = True
                mouse_controller.click(mouse.Button.left, 1)
                simulated_click['left'] = False
                print("Automatic left click")
    elif button_type == 'right':
        if time_between_clicks['right'] < rightMaxTimeBetweenClicks:
            for i in range(rightClicksCount):
                time.sleep(time_between_clicks['right'] / rightClicksCount)
                simulated_click['right'] = True
                mouse_controller.click(mouse.Button.right, 1)
                simulated_click['right'] = False
                print("Automatic right click")

# Configure the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Start the CPS checking thread
cps_thread = threading.Thread(target=check_cps)
cps_thread.start()

# Start the periodic updates thread
update_thread = threading.Thread(target=send_periodic_updates)
update_thread.start()

# Start the thread to monitor the status of menu.py
monitor_thread = threading.Thread(target=monitor_menu)
monitor_thread.start()

# Keep the script running
mouse_listener.join()
cps_thread.join()
update_thread.join()
monitor_thread.join()
