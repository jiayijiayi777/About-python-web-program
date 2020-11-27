# -*- coding: utf-8 -*-
# First run in the terminal: pip install requests
# Update your Chrome to the latest version
# Download the latest version at http://chromedriver.storage.googleapis.com/index.html
# Unzip the downloaded file and put it in the Scripts folder of your python installation directory

import requests  # Call the requests library
import time  # Call time library
from selenium import webdriver  # Invoke Chrome Drive

start_url = input('Please enter the URL, including http:')  # Set website link
driver = webdriver.Chrome()  # Use Chrome Drive
driver.get(url=start_url)  # open the Web page
time.sleep(5)  # Wait 5 seconds
driver.close()  # Close page
