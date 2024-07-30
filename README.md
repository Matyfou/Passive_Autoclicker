# Passive AutoClicker 

**Passive AutoClicker** is a Python-based automation tool that simulates mouse clicks based on user-defined settings. The tool is designed to automate mouse clicks for both left and right mouse buttons, offering custom click rates and intervals. The software can be configured to start and stop automatic clicking based on the number of clicks per second (CPS).

## Features

- **Customizable Click Settings:** Set parameters for both left and right clicks, including CPS thresholds to start and stop, interval checks, click counts, and maximum time between clicks.
- **Real-time Configuration:** The settings can be loaded and adjusted from a configuration file, allowing dynamic updates without restarting the application.
- **Simulated Clicks:** Performs automatic clicks when specific CPS thresholds are met.

## Installation

1. **You have to [Download python](https://www.python.org/downloads/release/python-3810/) (tested on 3.8.10 but probably works on others versions)**

2. **Download the repository or the release**

3. **Run the start script "start.bat"**

4. **Enjoy :)**

## How It Works

This script enhances user clicks by placing additional automatic clicks between user clicks. No need to define CPS (Clicks Per Second) since it uses the natural CPS from the user.

When the script detects user clicks, it multiplies them by the defined Clicks Count parameter. This process uses the user's click timing and inserts the additional clicks accordingly.

For example, if the user clicks three times per second and ClicksCount is set to 2, the script will generate two additional clicks for each user click, effectively increasing the click rate to 9 CPS using the user's base CPS (3+(3*2)).

## Demonstration

Here's a demonstration video on Minecraft showing quick switch between spamming and normal clicks without using any hotkey for automatic activation.

⠀
[![Watch the video](https://img.youtube.com/vi/DeVZcmNn2UE/0.jpg)](https://www.youtube.com/watch?v=DeVZcmNn2UE)


## Configuration Parameters

- **Click Parameters :**
    - `Start CPS`: Number of CPS needed to start the auto-clicking action .
    - `Stop CPS`: Number of CPS below which the auto-clicking action stops.
    - `Check Interval`: Interval (in seconds) to check CPS count. (Advanced)
    - `Clicks Count`: NNumber of clicks to perform after each user click. (Careful!)
    - `Max Time`: Max time after a user click to simulate a click.
    - `Enable`: Enable/disable automatic left/right clicks.

- **Recommended Values :**
    - `Start CPS`: 2-3 (reduce if activation takes too long)
    - `Stop CPS`: 1-2 (reduce if deactivation takes too long)
    - `Check Interval`: 0.10 (recommended to leave this unchanged)
    - `Clicks Count`: 1-3 (this is the main parameter to adjust, increase for more clicks !)
    - `Max Time`: 0.25-0.50 (if clicks are randomly doing after a spam)

## Disclaimer

Please be aware that using an autoclicker on platforms where it is prohibited, such as Minecraft, may violate the rules and result in penalties such as bans. Use this tool responsibly and only in contexts where it is allowed. 

I am not responsible for any issues, including bans or other penalties, that may arise from improper use of this autoclicker. Use at your own risk.