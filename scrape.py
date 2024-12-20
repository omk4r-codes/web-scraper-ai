import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_webpage(website):
    print("Launching Chrome...")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    driver.get(website)
    print("page loaded")
    html = driver.page_source
    return html

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return None
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_body_content = soup.get_text(separator="\n")
    clean_body_content = "\n".join(line.strip() for line in cleaned_body_content.splitlines() if line.strip())
    return cleaned_body_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]