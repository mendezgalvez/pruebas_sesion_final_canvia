import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        # codigo here!

    def test_reto_final_caso_arbitrario2(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        # codigo here!
    def test_reto_final_caso_arbitrario3(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        # codigo here!
    def test_reto_final_caso_arbitrario4(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        # codigo here!
    def test_reto_final_caso_arbitrario5(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")

        # codigo here!



if __name__ == '__main__':
    unittest.main()
