import time
import sys
sys.path.append('D:\test_framework\game')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from game.config import Config,DRIVER_PATH,DATA_PATH, REPORT_PATH
from game.log import  logger
from game.file_reader import ExcelReader
from game import HTMLTestRunner




class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel=DATA_PATH+'/baidu.xlsx'


    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()


    def test_search(self):
        datas=ExcelReader(self.excel).data
        for d in  datas:
            with self.subTest(data=d):
                self.sub.setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links=self.driver.find_element(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)
