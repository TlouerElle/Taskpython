from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import warnings


class Robot:
    def __init__(self):
        warnings.filterwarnings('ignore')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=self.options, executable_path='./chromedriver.exe')
        self.driver.get('https://kyfw.12306.cn/otn/resources/login.html')
        self.driver.maximize_window()

    def wait_ele_click_xpath_safe(self, xpath, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()

    def wait_ele_xpath_safe(self, xpath, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        if self.driver.find_element_by_xpath(xpath):
            return True
        else:
            return False

    def find_ele_click_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys_xpath(self, xpath, keys):
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(keys)

    def find_eles_xpath(self, xpath):
        eles = self.driver.find_elements_by_xpath(xpath)
        return eles

    def click_to_last_window_xpath(self, xpath):
        self.find_ele_click_xpath(xpath)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])

    def get_ele_text(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    def input_clear_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).clear()

    def switch_last_window(self):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])


robot = Robot()
