import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    mars = {
        "news title": news_title,
        "news paragraph": news_p,
        "featured image": featured_image_url,
        "weather": mars_weather,
        "hemispheres": hemisphere_image_urls
    }