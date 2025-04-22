import argparse
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

def search_google(query):
    urls = []
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = uc.Chrome(options=options)
    driver.get(f"https://www.google.com/search?q={query}")
    time.sleep(3)

    results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf > a')
    for r in results:
        urls.append(r.get_attribute('href'))

    driver.quit()
    return {"engine": "Google", "result_count": len(urls), "urls": urls}

def search_bing(query):
    urls = []
    driver = uc.Chrome(headless=True)
    driver.get(f"https://www.bing.com/search?q={query}")
    time.sleep(3)

    links = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')
    for link in links:
        href = link.get_attribute('href')
        if href:
            urls.append(href)

    driver.quit()
    return {"engine": "Bing", "result_count": len(urls), "urls": urls}

def search_yandex(query):
    urls = []
    driver = uc.Chrome(headless=True)
    driver.get(f"https://yandex.com/search/?text={query}")
    time.sleep(3)

    results = driver.find_elements(By.CSS_SELECTOR, 'h2 > a.link')
    for r in results:
        href = r.get_attribute('href')
        if href:
            urls.append(href)

    driver.quit()
    return {"engine": "Yandex", "result_count": len(urls), "urls": urls}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="Kata kunci atau email untuk pencarian")
    args = parser.parse_args()

    if not args.query:
        print("❌ Masukkan kata kunci dengan --query")
        exit()

    output = []
    try:
        output.append(search_google(args.query))
    except Exception as e:
        output.append({"engine": "Google", "error": str(e)})

    try:
        output.append(search_bing(args.query))
    except Exception as e:
        output.append({"engine": "Bing", "error": str(e)})

    try:
        output.append(search_yandex(args.query))
    except Exception as e:
        output.append({"engine": "Yandex", "error": str(e)})

    print(json.dumps(output, indent=2))
