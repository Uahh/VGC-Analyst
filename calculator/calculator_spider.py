import os
import re
import json
from copy import deepcopy
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

class Caclulator:
    def __init__(self):
        self.url = url
        self.export_json = export_json
        self.pokemon_dict = {
        }
        self.service = Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(30)