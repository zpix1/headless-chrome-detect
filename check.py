import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import getcwd


def test(name, /, userAgent=None, prerun=None):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1920,1080")
    if userAgent:
        options.add_argument(f"user-agent={userAgent}")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    if prerun:
        prerun(driver)

    driver.get(f"file://{getcwd()}/index.html")
    element = driver.find_element(By.ID, "result")
    log = driver.find_element(By.ID, "log")

    time.sleep(0.1)

    print(f"{name} result: {element.text}")
    print(log.get_attribute("value"))

    driver.quit()


test("Default headless")
test(
    "Fake UA headless",
    userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
)

def fixup(driver):
    script = '''
Object.defineProperty(navigator, 'webdriver', {
    get: () => false,
});
Object.defineProperty(window, 'chrome', {
    get: () => true,
});
Object.defineProperty(window, 'outerWidth', {
    get: () => 1920,
});
Object.defineProperty(window, 'outerHeight', {
    get: () => 1080,
});
'''
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': script})


test(
    "Fake UA headless + JS fixup",
    userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    prerun=fixup
)
