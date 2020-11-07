import base64
import logging
import os
import sys

from time import localtime, sleep, strftime, time

from selenium import webdriver
from selenium.common.exceptions import *


CV_DEFAULT_REFRESH_INTERVAL = 300 # 300 minutes = 5 hours
HH_DEFAULT_LOGLEVEL = 'INFO'

hh_username = os.getenv("HH_USERNAME")
hh_password = os.getenv("HH_PASSWORD")
hh_resumeid = os.getenv("HH_RESUMEID")
hh_loglevel = os.getenv("HH_LOGLEVEL", HH_DEFAULT_LOGLEVEL)
refresh_interval = os.getenv("CV_REFRESH_INTERVAL", CV_DEFAULT_REFRESH_INTERVAL)

hh_login_url = 'https://www.hh.ru/account/login'
login_input_xpath = '//*[@id="HH-React-Root"]/div/div/div[2]/div/div/form/div[1]/input'
password_input_xpath = '//*[@id="HH-React-Root"]/div/div/div[2]/div/div/form/div[2]/span/input'
submit_button_xpath = '//*[@id="HH-React-Root"]/div/div/div[2]/div/div/form/div[4]/button'
applicant_resumeid_url = f'https://hh.ru/resume/{hh_resumeid}'
refresh_button_byid_xpath = '//*[@id="HH-React-Root"]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/button'
applicant_resumes_url = 'https://hh.ru/applicant/resumes'
refresh_button_xpath = '//*[@id="HH-React-Root"]/div/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div/div/div[1]/span/button'

dcap = webdriver.DesiredCapabilities.PHANTOMJS.copy()
dcap['phantomjs.page.customHeaders.User-Agent'] = \
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/39.0.2171.95 Safari/537.36'
browser = webdriver.PhantomJS(desired_capabilities=dcap)

logging_datefmt = '%d-%b-%y %H:%M:%S'
logging_format = '%(asctime)s %(levelname)s %(message)s'
logging_level = logging.getLevelName(hh_loglevel)
logging.basicConfig(format=logging_format, datefmt=logging_datefmt, level=logging_level)


def hh_login():
    logging.info(f'hh_login: get {hh_login_url}')
    browser.get(hh_login_url)

    #  fill login
    login_input = browser.find_element_by_xpath(login_input_xpath)
    login_input.clear()
    login_input.send_keys(hh_username)

    #  fill password
    password_input = browser.find_element_by_xpath(password_input_xpath)
    password_input.clear()
    password_input.send_keys(hh_password)

    #  click 'submit'
    submit_button = browser.find_element_by_xpath(submit_button_xpath)
    submit_button.click()


def refresh_cv():
    if hh_resumeid:
        logging.info(f'refresh_cv: get {applicant_resumeid_url}')
        browser.get(applicant_resumeid_url)
        # NOTE To get refresh button's xpath toggle yor browser to "Mobile view" mode.
        # This is due to the fact that Selenium displays a narrow page by default.
        refresh_button = browser.find_element_by_xpath(refresh_button_byid_xpath)
    else:
        logging.info(f'refresh_cv: get {applicant_resumes_url}')
        browser.get(applicant_resumes_url)
        refresh_button = browser.find_element_by_xpath(refresh_button_xpath)

    if refresh_button:
        try:
            refresh_button.click()
        except Exception as e:
            print(e)


def main():
    logging.info('main: loop start')
    browser.delete_all_cookies()
    hh_login()
    refresh_cv()
    next_refresh_time = strftime('%c', localtime(time()+refresh_interval*60))
    logging.info(f'main: sleep for {refresh_interval} minutes, until {next_refresh_time}')
    sleep(int(refresh_interval)*60)


if __name__ == '__main__':
    while(True):
        try:
            main()
        except KeyboardInterrupt:
            sys.exit('Interrupted..')
        except NoSuchElementException as ex:
            logging.error(ex)
            with open('/tmp/screenshot.png', 'wb') as f:
                f.write(base64.decodebytes(ex.screen.encode()))
        except Exception as ex:
            logging.error(ex, exc_info=True)
