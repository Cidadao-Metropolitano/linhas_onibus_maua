import time
import pandas
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

url = "https://suzanturmaua.com.br/linhas/"


option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)

driver.quit()