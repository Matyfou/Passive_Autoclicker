import tkinter as tk
from tkinter import ttk
import pickle
import threading

# Create the main window
root = tk.Tk()
root.title("Passive Autoclicker | 1.0 | Matyfou")
root.geometry("800x750")  # Window size to accommodate both sections

# Global variables for left click
leftCpsToStart = 3
leftCpsToStop = 2
leftCpsTimeCheck = 0.1
leftClicksCount = 1
leftMaxTimeBetweenClicks = 0.4
leftEnabled = tk.BooleanVar(value=True)

# Global variables for right click
rightCpsToStart = 3
rightCpsToStop = 2
rightCpsTimeCheck = 0.1
rightClicksCount = 1
rightMaxTimeBetweenClicks = 0.4
rightEnabled = tk.BooleanVar(value=True)

# Lock to protect access to the config file
config_lock = threading.Lock()

# Function to update values and save to config file
def update_values():
    global leftCpsToStart, leftCpsToStop, leftCpsTimeCheck, leftClicksCount, leftMaxTimeBetweenClicks, leftEnabled
    global rightCpsToStart, rightCpsToStop, rightCpsTimeCheck, rightClicksCount, rightMaxTimeBetweenClicks, rightEnabled

    # Left click
    leftCpsToStart = left_cps_to_start_slider.get()
    leftCpsToStop = left_cps_to_stop_slider.get()
    leftCpsTimeCheck = left_cps_time_check_slider.get()
    leftClicksCount = left_clicks_count_slider.get()
    leftMaxTimeBetweenClicks = left_max_time_between_clicks_slider.get()
    leftEnabled.set(left_enable_checkbox_var.get())

    # Right click
    rightCpsToStart = right_cps_to_start_slider.get()
    rightCpsToStop = right_cps_to_stop_slider.get()
    rightCpsTimeCheck = right_cps_time_check_slider.get()
    rightClicksCount = right_clicks_count_slider.get()
    rightMaxTimeBetweenClicks = right_max_time_between_clicks_slider.get()
    rightEnabled.set(right_enable_checkbox_var.get())

    save_config()

# Function to save values to the config file
def save_config():
    config = {
        "leftCpsToStart": leftCpsToStart,
        "leftCpsToStop": leftCpsToStop,
        "leftCpsTimeCheck": leftCpsTimeCheck,
        "leftClicksCount": leftClicksCount,
        "leftMaxTimeBetweenClicks": leftMaxTimeBetweenClicks,
        "leftEnabled": leftEnabled.get(),
        "rightCpsToStart": rightCpsToStart,
        "rightCpsToStop": rightCpsToStop,
        "rightCpsTimeCheck": rightCpsTimeCheck,
        "rightClicksCount": rightClicksCount,
        "rightMaxTimeBetweenClicks": rightMaxTimeBetweenClicks,
        "rightEnabled": rightEnabled.get()
    }
    with config_lock:
        with open('config.pkl', 'wb') as f:
            pickle.dump(config, f)

# Function to load values from the config file
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
                leftEnabled.set(config["leftEnabled"])

                # Right click
                rightCpsToStart = config["rightCpsToStart"]
                rightCpsToStop = config["rightCpsToStop"]
                rightCpsTimeCheck = config["rightCpsTimeCheck"]
                rightClicksCount = config["rightClicksCount"]
                rightMaxTimeBetweenClicks = config["rightMaxTimeBetweenClicks"]
                rightEnabled.set(config["rightEnabled"])
    except FileNotFoundError:
        pass

# Load configuration on startup
load_config()

# Initialize sliders with the loaded or default values
def initialize_sliders():
    left_cps_to_start_slider.set(leftCpsToStart)
    left_cps_to_stop_slider.set(leftCpsToStop)
    left_cps_time_check_slider.set(leftCpsTimeCheck)
    left_clicks_count_slider.set(leftClicksCount)
    left_max_time_between_clicks_slider.set(leftMaxTimeBetweenClicks)

    right_cps_to_start_slider.set(rightCpsToStart)
    right_cps_to_stop_slider.set(rightCpsToStop)
    right_cps_time_check_slider.set(rightCpsTimeCheck)
    right_clicks_count_slider.set(rightClicksCount)
    right_max_time_between_clicks_slider.set(rightMaxTimeBetweenClicks)

# Create frames to separate left and right click configurations
left_frame = tk.Frame(root, padx=10, pady=10)
right_frame = tk.Frame(root, padx=10, pady=10)
bottom_frame = tk.Frame(root, pady=10)  # Frame for the "Quit" button

# Create titles for the sections
left_title = ttk.Label(left_frame, text="LEFT CLICK", font=("Arial", 16, "bold"))
right_title = ttk.Label(right_frame, text="RIGHT CLICK", font=("Arial", 16, "bold"))

# Create sliders for left click
left_cps_to_start_slider = tk.Scale(left_frame, from_=1, to=10, orient="horizontal", label="Start CPS",
                                    command=lambda x: update_values())
left_cps_to_stop_slider = tk.Scale(left_frame, from_=1, to=10, orient="horizontal", label="Stop CPS",
                                   command=lambda x: update_values())
left_cps_time_check_slider = tk.Scale(left_frame, from_=0.05, to=1, orient="horizontal", resolution=0.05,
                                      label="Check Interval", command=lambda x: update_values())
left_clicks_count_slider = tk.Scale(left_frame, from_=1, to=5, orient="horizontal", label="Clicks Count",
                                    command=lambda x: update_values())
left_max_time_between_clicks_slider = tk.Scale(left_frame, from_=0.05, to=1, orient="horizontal", resolution=0.05,
                                               label="Max Time", command=lambda x: update_values())

# Create sliders for right click
right_cps_to_start_slider = tk.Scale(right_frame, from_=1, to=10, orient="horizontal", label="Start CPS",
                                     command=lambda x: update_values())
right_cps_to_stop_slider = tk.Scale(right_frame, from_=1, to=10, orient="horizontal", label="Stop CPS",
                                    command=lambda x: update_values())
right_cps_time_check_slider = tk.Scale(right_frame, from_=0.05, to=1, orient="horizontal", resolution=0.05,
                                       label="Check Interval", command=lambda x: update_values())
right_clicks_count_slider = tk.Scale(right_frame, from_=1, to=5, orient="horizontal", label="Clicks Count",
                                     command=lambda x: update_values())
right_max_time_between_clicks_slider = tk.Scale(right_frame, from_=0.05, to=1, orient="horizontal", resolution=0.05,
                                                label="Max Time", command=lambda x: update_values())

# Create description labels for left click
left_cps_to_start_label = ttk.Label(left_frame, text="Number of CPS needed to start the auto-clicking action.", wraplength=350)
left_cps_to_stop_label = ttk.Label(left_frame, text="Number of CPS below which the auto-clicking action stops.", wraplength=350)
left_cps_time_check_label = ttk.Label(left_frame, text="Interval (in seconds) to check CPS count. (Advanced)", wraplength=350)
left_clicks_count_label = ttk.Label(left_frame, text="Number of clicks to perform after each user click. (Careful!)", wraplength=350)
left_max_time_between_clicks_label = ttk.Label(left_frame, text="Max time after a user click to simulate a click", wraplength=350)

# Create description labels for right click
right_cps_to_start_label = ttk.Label(right_frame, text="Number of CPS needed to start the auto-clicking action.", wraplength=350)
right_cps_to_stop_label = ttk.Label(right_frame, text="Number of CPS below which the auto-clicking action stops.", wraplength=350)
right_cps_time_check_label = ttk.Label(right_frame, text="Interval (in seconds) to check CPS count. (Advanced)", wraplength=350)
right_clicks_count_label = ttk.Label(right_frame, text="Number of clicks to perform after each user click. (Careful!)", wraplength=350)
right_max_time_between_clicks_label = ttk.Label(right_frame, text="Max time after a user click to simulate a click", wraplength=350)

# Create checkboxes
left_enable_checkbox_var = tk.BooleanVar(value=True)
right_enable_checkbox_var = tk.BooleanVar(value=True)

left_enable_checkbox = ttk.Checkbutton(left_frame, text="Enable Left Click", variable=left_enable_checkbox_var,
                                       command=update_values)
right_enable_checkbox = ttk.Checkbutton(right_frame, text="Enable Right Click", variable=right_enable_checkbox_var,
                                        command=update_values)

# Place widgets for left click
left_title.pack(pady=(0, 10))
left_enable_checkbox.pack(pady=(0, 10))  # Place the checkbox
left_cps_to_start_label.pack(pady=(0, 5))
left_cps_to_start_slider.pack(pady=(0, 10))
left_cps_to_stop_label.pack(pady=(0, 5))
left_cps_to_stop_slider.pack(pady=(0, 10))
left_cps_time_check_label.pack(pady=(0, 5))
left_cps_time_check_slider.pack(pady=(0, 10))
left_clicks_count_label.pack(pady=(0, 5))
left_clicks_count_slider.pack(pady=(0, 10))
left_max_time_between_clicks_label.pack(pady=(0, 5))
left_max_time_between_clicks_slider.pack(pady=(0, 10))

# Place widgets for right click
right_title.pack(pady=(0, 10))
right_enable_checkbox.pack(pady=(0, 10))  # Place the checkbox
right_cps_to_start_label.pack(pady=(0, 5))
right_cps_to_start_slider.pack(pady=(0, 10))
right_cps_to_stop_label.pack(pady=(0, 5))
right_cps_to_stop_slider.pack(pady=(0, 10))
right_cps_time_check_label.pack(pady=(0, 5))
right_cps_time_check_slider.pack(pady=(0, 10))
right_clicks_count_label.pack(pady=(0, 5))
right_clicks_count_slider.pack(pady=(0, 10))
right_max_time_between_clicks_label.pack(pady=(0, 5))
right_max_time_between_clicks_slider.pack(pady=(0, 10))

# Place frames
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="right", fill="both", expand=True)
bottom_frame.pack(side="bottom", fill="x")

# Add the "Quit" button
quit_button = tk.Button(bottom_frame, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Initialize sliders with the loaded or default values
initialize_sliders()

# Start the application
root.mainloop()
