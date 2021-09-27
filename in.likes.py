from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import pw
import os


class InstagramBot:
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome('C:\Python\chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get(
            '{}'.format(self.base_url))
        sleep(3)

        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/button[1]').click()

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        self.driver.find_element_by_css_xpath(
            ".//*[contains(text(), 'save Info')]").click()

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))
        self.driver.get('instagram account link')

    def like_latest_posts(self, user, n_posts, like=True):

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click()
            sleep(1)
            try:
                self.driver.find_element_by_xpath(
                    "//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)

            self.driver.find_elements_by_class_name('ckWGn')[0].click()


if __name__ == "__main__":
    ig_bot = InstagramBot('insta_name', pw)

    ig.bot.nav_user('insta_name')
