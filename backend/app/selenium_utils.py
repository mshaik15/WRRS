from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_title(url: str) -> str:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    title = driver.title
    driver.quit()
    return title
