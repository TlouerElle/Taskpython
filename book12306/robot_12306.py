import time
import traceback

from loguru import logger

from robot import Robot
from localconfig import config


class robot_12306(Robot):
    def __init__(self):
        super().__init__()
        self.travel_list = []
        self.config = config

    def prepare(self):
        self.log_t(self.config)
        config_values_list = list(self.config.values())
        if not all(config_values_list):
            raise self.log_t('config缺少或不存在')

    def login(self):
        self.log_t('start logining')
        time.sleep(1)
        if self.find_ele_xpath('//*[@id="ERROR"]'):
            self.wait_ele_click_xpath_safe('//a[@id="login_user"]')
        self.wait_ele_click_xpath_safe('//li[@class="login-hd-account"]')
        try:
            if self.wait_ele_xpath_safe('//li[@class="nav-item nav-item-w1"]', timeout=60):
                self.log_t('login success')
                session_id = self.driver.session_id
                self.driver.session_id = session_id
        except TimeoutError as e:
            self.log_t(f'login timeout:{e}')
        except Exception as e:
            self.log_t(f'login false:{traceback.format_exc()}')

    @logger.catch
    def check_time(self):
        self.log_t('start checking time')
        time.sleep(5)
        self.wait_ele_click_xpath_safe('//*[@id="J-xinxichaxun"]/a')
        self.wait_ele_click_xpath_safe('//*[@id="megamenu-9"]/div[1]/ul/li[5]/a')
        # todo 查询车票放票时间
        self.input_clear_xpath('//*[@id="sale_time_date"]')
        self.send_keys_xpath('//*[@id="sale_time_date"]', self.config['travel_date'])
        self.find_ele_click_xpath('//*[@id="saleText"]')
        self.send_keys_xpath('//*[@id="saleText"]', self.config['start_station'])
        self.find_ele_click_xpath('//*[@id="citem_0"]')
        check_time = ''
        self.wait_ele_xpath_safe('//*[@id="sale-time1"]/div[1]/ul/li')
        rows = self.find_eles_xpath('//*[@id="sale-time1"]/div[1]/ul/li')
        for row in rows:
            station = row.find_element_by_xpath('.//div[@class="sale-station-name"]').text
            if self.config['start_station']+'站' in station:
                check_time = row.find_element_by_xpath('/div[@class="sale-time"]').text.repalace('起售', '')
        if not check_time:
            raise '查询起售日期的起售时间失败'




    @logger.catch
    def book(self):
        self.log_t('start booking')
        self.find_ele_click_xpath('//li[@class="nav-item nav-item-w1"]')
        self.wait_ele_click_xpath_safe('//*[@id="fromStationText"]')
        self.send_keys_xpath('//*[@id="fromStationText"]', self.config['start_station'])
        self.find_ele_click_xpath('//*[@id="citem_0"]')
        self.send_keys_xpath('//*[@id="toStationText"]', self.config['to_station'])
        self.find_ele_click_xpath('//*[@id="citem_0"]')
        self.send_keys_xpath('//*[@id="train_date"]', self.config['travel_date'])
        self.click_to_last_window_xpath('//*[@id="search_one"]')
        self.log_t('search success')
        # todo 检查起售时间才能继续
        if self.find_ele_xpath('//*[@id="no_filter_ticket_6"]/p'):
            self.log_t('出发日时间不允许')
            self.close_window()
            return
        table = '/html/body/div[2]/div[8]/div[8]/table/tbody/tr'
        self.wait_ele_xpath_safe(table)
        rows = self.find_eles_xpath(table)
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
            self.log_t(got_travel)
            self.travel_list.append(got_travel)
            if start_station == self.config['start_station'] and to_station == self.config[
                'to_station'] and start_time == self.config['start_time'] and to_time == self.config[
                'to_time'] and is_have != '候补':
                row.find_element_by_xpath('.//td/a').click()
                time.sleep(1)
                if self.find_ele_xpath('//div[@id="content_defaultwarningAlert_hearder"]'):
                    hint = self.get_ele_text('//div[@id="content_defaultwarningAlert_hearder"]')
                    self.close_window()
                    raise self.log_t(f'{hint}')
                self.wait_ele_xpath_safe('//*[@id="normal_passenger_id"]/li', timeout=10)
                choices = self.find_eles_xpath('//*[@id="normal_passenger_id"]/li')
                for choice in choices:
                    person = choice.find_element_by_xpath('./label').text
                    if self.config['travel_person'] in person:
                        choice.find_element_by_xpath('./input').click()
                        break
                #  todo 请检查，可能出现乘车人不存在的情况目前想到any这一系列方法
                self.log_t('请检查，可能出现乘车人不存在的情况')
                self.find_ele_click_xpath('//a[text()="提交订单"]')
                site = f'//*[@id="erdeng1"]/ul/li/a[@id="1{self.config["seat"]}"]'
                time.sleep(5)
                self.wait_ele_click_xpath_safe(site)
                self.find_ele_click_xpath('//*[@id="qr_submit_id"]')
                time.sleep(5)
                if self.wait_ele_xpath_safe('//*[@id="orderResultInfo_id"]/p'):
                    hint = self.get_ele_text('//*[@id="orderResultInfo_id"]/p')
                    if '抱歉' in hint:
                        raise self.log_t(f'订票失败，{hint}')
                    else:
                        self.log_t('成功, 若当日已经购票且时间冲突,12306则会在查询页面显示为订票失败')
                break
