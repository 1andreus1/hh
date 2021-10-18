from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

try:
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)
    browser.get('https://duckduckgo.com')
    print(browser.page_source)
finally:
    browser.close()
    browser.quit()