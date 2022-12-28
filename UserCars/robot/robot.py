import time
import csv
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger


def logging(msg):
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.add(r'D:\pythonProject\UserCars\log\file_{time}.log')
    logger.info(f'{msg}')


def checking(text):
    print(f'\033[1;31m{text}\033[0m')


def writeCsv(line):
    with open(r'cars.csv', 'a+', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(line)


def robot(url, set_count):
    robot = webdriver.Chrome('./chromedriver.exe')
    robot.maximize_window()
    robot.get(url)
    count = 1
    try:
        while robot.find_element(By.XPATH, '//a[@id="morecars"]') and count <= set_count:
            robot.find_element(By.XPATH, '//a[@id="morecars"]').click()
            checking(f'No.{count} click to loading')
            time.sleep(1)
            count += 1
        checking('Next, start traversing!!')
        rows = robot.find_elements(By.XPATH, '//p[@class="cal_main_title"]/a')
        for row in rows:
            robot.execute_script("arguments[0].click();", row)
            windows = robot.window_handles
            robot.switch_to.window(windows[-1])
            checking(f'loading:{robot.current_url}')
            release_data = robot.find_element(By.XPATH, '//div[@class="fr"]').text
            title = robot.find_element(By.XPATH, '//h1').text
            purpose = robot.find_element(By.XPATH,
                                         '//div[@class="datum_right"]/div[@class="new_tag"]/div[@class="tag_item '
                                         'tag_blue"]/span').text
            owner_quote = robot.find_element(By.XPATH, '//span[1]/b').text
            reference_price = robot.find_element(By.XPATH, '//span[@class="c9"][1]').text
            new_price = robot.find_element(By.XPATH, '//span[@class="c9"][2]').text
            vehicle_condition = robot.find_elements(By.XPATH, '//div[@id="cut_list1"]/div[@class="parameter"]//dt')
            licensing_data = vehicle_condition[0].text
            table_mileage = vehicle_condition[1].text
            licensing_site = vehicle_condition[2].text
            displacement = vehicle_condition[3].text
            transmission_case = vehicle_condition[4].text
            environmental_standards = vehicle_condition[5].text
            insurance_end = vehicle_condition[6].text
            inspect_end = vehicle_condition[7].text
            brand = robot.find_element(By.XPATH,
                                       '//div[@id="basic_par"][1]/table/tbody/tr[2]/td[@class="rh_txt"][1]').text
            checking(
                f'{release_data},{title},{purpose},{owner_quote},{reference_price},{new_price},{licensing_data},{table_mileage},{licensing_site},{displacement},{transmission_case},{environmental_standards},{insurance_end},{inspect_end},{brand}')
            line = [release_data, title, purpose, owner_quote, reference_price, new_price, licensing_data,
                    table_mileage, licensing_site, displacement, transmission_case, environmental_standards, insurance_end, inspect_end, brand]
            writeCsv(line)
            time.sleep(1)
            robot.close()
            robot.switch_to.window(windows[0])

    except Exception:
        logging(f'The number of clicks to load is {count} ,{robot.current_url},{traceback.format_exc()}')
    checking('All finish')


if __name__ == '__main__':
    # url访问目标index
    # set_count点击加载更多次数
    url = 'https://used.xcar.com.cn/search/100-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0/'
    set_count = 500
    robot(url, set_count)
