from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    print('Connecting to remote debugging Chrome...')

    options = Options()
    options.debugger_address = "localhost:9222"  # Connect to already running Chrome

    driver = webdriver.Chrome(options=options)

    print('Connected! Navigating to https://google.com...')
    driver.get('https://google.com')

    print('Navigated! Scraping page content...')
    html = driver.page_source
    print(html)

    driver.quit()

if __name__ == '__main__':
    main()
