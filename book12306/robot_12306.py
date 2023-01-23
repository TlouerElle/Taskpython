import time
import traceback

from loguru import logger

import robot
from localconfig import config


class robot_12306:
    def __init__(self):
        self.robot = robot.Robot()
        self.travel_list = []
        self.config = config

    def prepare(self):
        self.robot.log_t(self.config)
        config_values_list = list(self.config.values())
        if not all(config_values_list):
            raise self.robot.log_t('config缺少或不存在')

    def login(self):
        self.robot.log_t('start logining')
        self.robot.wait_ele_click_xpath_safe('//li[@class="login-hd-account"]')
        try:
            if self.robot.wait_ele_xpath_safe('//li[@class="nav-item nav-item-w1"]', timeout=60):
                self.robot.log_t('login success')
        except TimeoutError as e:
            self.robot.log_t(f'login timeout:{e}')
        except Exception as e:
            self.robot.log_t(f'login false:{traceback.format_exc()}')

    @logger.catch
    def book(self):
        self.robot.log_t('start booking')
        time.sleep(5)
        self.robot.find_ele_click_xpath('//li[@class="nav-item nav-item-w1"]')
        self.robot.wait_ele_click_xpath_safe('//*[@id="fromStationText"]')
        self.robot.send_keys_xpath('//*[@id="fromStationText"]', self.config['start_station'])
        self.robot.find_ele_click_xpath('//*[@id="citem_0"]')
        self.robot.send_keys_xpath('//*[@id="toStationText"]', self.config['to_station'])
        self.robot.find_ele_click_xpath('//*[@id="citem_0"]')
        self.robot.send_keys_xpath('//*[@id="train_date"]', self.config['travel_date'])
        self.robot.click_to_last_window_xpath('//*[@id="search_one"]')
        self.robot.log_t('search success')
        table = '/html/body/div[2]/div[8]/div[8]/table/tbody/tr'
        self.robot.wait_ele_xpath_safe(table)
        rows = self.robot.find_eles_xpath(table)
        for row in rows:
            if row.get_attribute('style') == 'display: none;':
                continue
            car_number = row.find_element_by_xpath('.//div/a').text
            start_station = row.find_element_by_xpath('./td[1]/div/div[2]/strong[1]').text
            to_station = row.find_element_by_xpath('./td[1]/div/div[2]/strong[2]').text
            start_time = row.find_element_by_xpath('./td[1]/div/div[3]/strong[1]').text
            to_time = row.find_element_by_xpath('./td[1]/div/div[3]/strong[2]').text
            is_have = row.find_element_by_xpath('./td[4]').text
            got_travel = {'car_number': car_number,
                          'start_station': start_station,
                          'to_station': to_station,
                          'start_time': start_time,
                          'to_time': to_time,
                          'is_have': is_have,
                          }
            self.robot.log_t(got_travel)
            self.travel_list.append(got_travel)
            if start_station == self.config['start_station'] and to_station == self.config[
                'to_station'] and start_time == self.config['start_time'] and to_time == self.config[
                'to_time'] and is_have != '候补':
                row.find_element_by_xpath('.//td/a').click()
                self.robot.wait_ele_xpath_safe('//*[@id="normal_passenger_id"]/li', timeout=10)
                choices = self.robot.find_eles_xpath('//*[@id="normal_passenger_id"]/li')
                for choice in choices:
                    person = choice.find_element_by_xpath('./label').text
                    if self.config['travel_person'] in person:
                        choice.find_element_by_xpath('./input').click()
                        break
                #  todo 请检查，可能出现乘车人不存在的情况目前想到any这一系列方法
                self.robot.log_t('请检查，可能出现乘车人不存在的情况')
                self.robot.find_ele_click_xpath('//a[text()="提交订单"]')
                site = f'//*[@id="erdeng1"]/ul/li/a[@id="1{self.config["seat"]}"]'
                time.sleep(5)
                self.robot.wait_ele_click_xpath_safe(site)
                self.robot.find_ele_click_xpath('//*[@id="qr_submit_id"]')
                time.sleep(5)
                if self.robot.wait_ele_xpath_safe('//*[@id="orderResultInfo_id"]/p'):
                    hint = self.robot.get_ele_text('//*[@id="orderResultInfo_id"]/p')
                    if '抱歉' in hint:
                        raise self.robot.log_t(f'订票失败，{hint}')
                    else:
                        # todo 将更好适配这一情况
                        self.robot.log_t('成功, 若当日已经购票且时间冲突,12306则会在查询页面显示为订票失败')
                break
