from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.amazon.com/gp/product/B0054E8QYE/ref=x_gr_w_bb_sin?ie=UTF8&tag=x_gr_w_bb_sin-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=B0054E8QYE&SubscriptionId=1MGPYB6YW3HWK55XCGG2"


if __name__ == '__main__':
    # # 初始化浏览器
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1280,1024")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # self.driver = webdriver.Chrome()
    # self.driver.set_window_size(1920, 1080)
    driver.get(url)
    submit = driver.find_element_by_css_selector('#upsell-button')
    submit.click()
    # upsell - button

#     print(11)