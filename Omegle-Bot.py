# Made by Popcornjames
# If used please give me some credit
# This is my first time coding so there maybe some bugs
# This was made to work not to work fast. :)
# Check for updates on the Github page
# Version 1.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "THE PATH WHERE YOUR CHROME DRIVER IS"
driver = webdriver.Chrome(PATH)

j = 1
i = 1

while j <= 99999:
    driver.get("https://www.omegle.com/")

    time.sleep(3)

    click_button = driver.find_element_by_id("textbtn")
    click_button.click()
    i = 1
    print("Starting")

    while i <= 5:
        time.sleep(1)

        try:
            search = driver.find_element_by_class_name("chatmsg")
            search.send_keys("PUT WHAT YOU WANT THE BOT TO SAY HERE")
#Replace the " PUT WHAT YOU WANT THE BOT TO SAY HERE " with the message you want the bot to say.
            search.send_keys(Keys.RETURN)
            search.send_keys(Keys.ESCAPE)
            search.send_keys(Keys.ESCAPE)
            time.sleep(15)
#Replace the " 15 " with the amount of time you want the bot to wait befor starting again
            click_button = driver.find_element_by_class_name("disconnectbtn")
            click_button.click()
        except:
            click_button = driver.find_element_by_class_name("disconnectbtn")
            click_button.click()
            print("Failed")
        i = i + 1
        print(i)
    print("Done J=")
    print(j)
    print("Starting again")
    j = j + 1

