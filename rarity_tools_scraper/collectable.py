import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_COLLECTABLE_VIEW_URL = "https://rarity.tools/{collection}/view/{id}"
ua = UserAgent()


def get_collectable_data(collection: str, collectable: str):
	options = Options()
	options.headless = True

	driver = webdriver.Chrome(options=options)
	driver.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["https://lh3.googleusercontent.com"]})
	driver.execute_cdp_cmd('Network.enable', {})

	driver.get(BASE_COLLECTABLE_VIEW_URL.format(collection=collection, id=collectable))

	print(text)
