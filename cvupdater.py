import os
import time
from selenium import webdriver

hh_username = os.environ["HH_USERNAME"]
hh_password = os.environ["HH_PASSWORD"]

if "CV_REFRESH_INTERVAL" in os.environ:
    refresh_interval = os.environ["CV_REFRESH_INTERVAL"]
else:
    refresh_interval = 300

dcap = webdriver.DesiredCapabilities.PHANTOMJS.copy()
dcap['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
                                                                  'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                                  'Chrome/39.0.2171.95 Safari/537.36'
browser = webdriver.PhantomJS(desired_capabilities=dcap)


def hh_login():
    browser.get("https://www.hh.ru/account/login")

    #  fill login
    login_input = browser.find_element_by_name("username")
    login_input.clear()
    login_input.send_keys(hh_username)

    #  fill password
    password_input = browser.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(hh_password)

    #  click "submit"
    submit_button = browser.find_element_by_xpath("//input[@type='submit']")
    submit_button.click()


def refresh_cv():
    browser.get('https://hh.ru/applicant/resumes')
    time.sleep(5)
    #  find refresh button
    refresh_button = browser.find_element_by_xpath("//div[@id='HH-React-Root']//div[3]//div[1]//div[5]//div[1]//div[1]//div[1]//div[1]//span[1]//button[1]")

    if refresh_button:
        try:
            refresh_button.click()
        except Exception as e:
            print(e)


def main():
    time.sleep(2)
    browser.delete_all_cookies()
    hh_login()
    refresh_cv()

if __name__ == '__main__':
    while(True):
        try:
            main()
            time.sleep(int(refresh_interval)*60)
        except Exception as ex:
            print(ex)
