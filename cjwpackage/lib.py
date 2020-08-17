# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for cjwpackage Project
"""

from os.path import split
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary




def try_me():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    play = driver.find_element_by_class_name('ytp-large-play-button')
    screen = driver.find_element_by_class_name('ytp-fullscreen-button')
    screen.click()
    play.click()

if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import cjwpackage
    folder_source, _ = split(cjwpackage.__file__)
    # try_me()
