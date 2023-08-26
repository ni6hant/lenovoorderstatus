import pygame
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from datetime import timedelta

# Constants
ORDER_NUMBER = "4321012345" #Your Order Number
EMAIL = "test@gmail.com" #Your Email ID
HOURS = 0.5 # Hours
CHECK_INTERVAL = int(timedelta(hours=HOURS).total_seconds())  # seconds

# Initialize the web driver
driver = webdriver.Chrome()

# Initialize pygame
pygame.init()

# Maximize the browser window
driver.maximize_window()

previous_order_status = None

while True:
    # Open the website
    driver.get("https://www.lenovo.com/in/en/vinculum/orderstatus")

    # Wait for the dialog to appear
    time.sleep(5)  # Adjust the time based on how long it takes for the dialog to appear
    
    # Check if the dialog is present and close it if it is
    try:
        close_button = driver.find_element(By.XPATH, "//div[@class='Q14020_popup_mainDiv']//a")
        close_button.click()
    except:
        pass
    
    # Wait for a short moment after closing the dialog
    time.sleep(3)

    # Find and fill the order number and email fields
    order_number_input = driver.find_element(By.NAME, "orderNumber")
    order_number_input.send_keys(ORDER_NUMBER)

    email_input = driver.find_element(By.NAME, "guestEmail")
    email_input.send_keys(EMAIL)

    # Click on the "Check Status" button
    check_status_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Check Status')]")
    check_status_button.click()

    # Wait for the redirect and page load
    time.sleep(5)

    # Find the order status element and get its text
    order_status_element = driver.find_element(By.XPATH, "//div[@class='orderStatus']")
    order_status = order_status_element.text
    print("Order Status:", order_status)

    # If the order status has changed, download and play the audio file
    if order_status != previous_order_status:
        if previous_order_status is not None:
            previous_order_status = order_status
            audio_url = "http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg"
            
            # Download the audio file
            audio_response = requests.get(audio_url)
            with open("audio.ogg", "wb") as audio_file:
                audio_file.write(audio_response.content)
            
            # Play the downloaded audio file
            pygame.mixer.music.load("audio.ogg")
            pygame.mixer.music.play()

    # Display progress bar for time to next iteration
    for _ in range(CHECK_INTERVAL):
        time_remaining = CHECK_INTERVAL - _
        hours_remaining = time_remaining // 3600
        minutes_remaining = (time_remaining % 3600) // 60
        seconds_remaining = time_remaining % 60

        progress = int((_ / CHECK_INTERVAL) * 20)
        print("\rWaiting [{}{}] {:02d}:{:02d}:{:02d}".format("=" * progress, " " * (20 - progress),
                                                            hours_remaining, minutes_remaining, seconds_remaining), end="")
        time.sleep(1)


# Close the browser window (this part won't be reached in an infinite loop)
driver.quit()
