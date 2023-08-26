# Lenovo Order Status Checker

This Python script automatically checks the order status of your Lenovo purchase and plays an audio notification if the status changes.

## Prerequisites
- Windows Operating System. I have tested on Linux though.
- [Python](https://www.python.org/downloads/) installed on your computer.
- Google Chrome browser installed.
- An active internet connection.

## Setup

### Install Dependencies:

1. Open the command prompt and navigate to the project directory.
2. Create and activate a virtual environment by running these commands:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Download Chromedriver:

- Download the [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) executable that matches your Google Chrome browser version.
- Place the `chromedriver.exe` file in the project directory.

### Update Constants:

1. Open `main.py` in a text editor.
2. Update the following constants with your order details:

    ```python
    ORDER_NUMBER = "Your Order Number"
    EMAIL = "Your Email"
    CHECK_INTERVAL = 60  # seconds (interval between checks)
    ```

### Run the Script:

1. In the command prompt, navigate to the project directory and activate the virtual environment if you haven't already:

    ```bash
    venv\Scripts\activate
    ```

2. Run the script:

    ```bash
    python main.py
    ```

   The script will open a Google Chrome window and start checking the order status at the specified interval. It will play an audio notification if the status changes to the desired state.

### Exit the Script:

To stop the script, press `Ctrl+C` in the command prompt.

## Notes

- The script will continue running until you manually stop it.
- Make sure to keep the virtual environment activated when running the script each time.
