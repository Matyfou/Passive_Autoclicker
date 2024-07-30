# Passive AutoClicker 

**Passive AutoClicker** is a Python-based automation tool that simulates mouse clicks based on user-defined settings. The tool is designed to automate mouse clicks for both left and right mouse buttons, offering custom click rates and intervals. The software can be configured to start and stop automatic clicking based on the number of clicks per second (CPS).

## Features

- **Customizable Click Settings:** Set parameters for both left and right clicks, including CPS thresholds to start and stop, interval checks, click counts, and maximum time between clicks.
- **Real-time Configuration:** The settings can be loaded and adjusted from a configuration file, allowing dynamic updates without restarting the application.
- **Simulated Clicks:** Performs automatic clicks when specific CPS thresholds are met.

## Installation

1. **Download the repository or the release**

2. **Run the start script "start.bat"**

## How It Works

This script enhances user clicks by placing additional automatic clicks between user clicks. No need to define CPS (Clicks Per Second) since it uses the natural CPS from the user.

When the script detects user clicks, it multiplies them by the defined Clicks Count parameter. This process uses the user's click timing and inserts the additional clicks accordingly.

For example, if the user clicks three times per second and ClicksCount is set to 2, the script will generate two additional clicks for each user click, effectively increasing the click rate to 9 CPS using the user's base CPS (3+(3*2)).

## Configuration Parameters

- **Click Parameters:**
    - `Start CPS`: Number of CPS needed to start the auto-clicking action.
    - `Stop CPS`: Number of CPS below which the auto-clicking action stops.
    - `Check Interval`: Interval (in seconds) to check CPS count. (Advanced)
    - `Clicks Count`: NNumber of clicks to perform after each user click. (Careful!)
    - `Max Time`: Max time after a user click to simulate a click.
    - `Enable`: Enable/disable automatic left/right clicks.

