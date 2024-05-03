from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.duyuruvehaberlerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os

class TestDuyuruveHaberlerim:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementInvisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
    
    def waitForElementPresent(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
    
    def waitForElementClickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
    
    def pre_condition(self):
        userNameInput = self.waitForElementVisible(USER_XPATH)
        passwordInput = self.waitForElementVisible(PASSWORD_XPATH)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,userName)
        actions.send_keys_to_element(passwordInput,password)
        actions.click(loginButton)
        actions.perform()
        loginVerified = self.waitForElementVisible(LOGINVERIFIED_CSS)
        assert loginVerified.text == login_verified_text 
        closeLoginVerified = self.waitForElementClickable(CLOSELOGINVERIFIED_CSS)
        closeLoginVerified.click()
        announcements = self.waitForElementVisible(ANNOUNCEMENTS_XPATH)
        announcements.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        showMoreButton = self.waitForElementVisible(SHOWMOREBUTTON_CSS)
        showMoreButton.click()
        sleep(5)
    
    def test_success(self):
        self.pre_condition()
        searchBar = self.waitForElementVisible(SEARCHBAR_CSS)
        actions2 = ActionChains(self.driver)
        actions2.click(searchBar)
        actions2.send_keys_to_element(searchBar, "Yeni Gelenler İçin Bilgilendirme")
        actions2.perform()
        result1 = self.waitForElementVisible(RESULT1_XPATH)
        assert result1.text == result1_text
        result2 = self.waitForElementVisible(RESULT2_XPATH)
        assert result2.text == result2_text
        result3 = self.waitForElementVisible(RESULT3_XPATH)
        assert result3.text == result3_text

    def test_blank_results(self):
        self.pre_condition()
        searchBar = self.waitForElementVisible(SEARCHBAR_CSS)
        actions2 = ActionChains(self.driver)
        actions2.click(searchBar)
        actions2.send_keys_to_element(searchBar, "x")
        actions2.perform()
        result4 = self.waitForElementVisible(RESULT4_XPATH)
        assert result4.text == result4_text

    def test_type_listing(self):
        self.pre_condition()
        typeBar = self.waitForElementVisible(TYPEBAR_XPATH) 
        typeBar.click()
        option2 = self.waitForElementVisible(OPTION2_ID)
        option2.click()
        typeBar.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,100)")
        selectedpage1 = self.waitForElementVisible(SELECTEDPAGE1_CSS)
        assert selectedpage1.text == selectedpage1_text
        sleep(2)
        listOfResults = self.driver.find_elements(LISTOFRESULTS_CSS)
        assert len(listOfResults) ==9
        sleep(5)

    def test_blank_type_listing(self):
        self.pre_condition()
        typeBar = self.waitForElementVisible(TYPEBAR_XPATH) 
        typeBar.click()
        option1 = self.waitForElementVisible(OPTION1_ID)
        option1.click()
        typeBar.click()
        sleep(2) #bu sleep olmayınca görmüyor
        result5 = self.waitForElementVisible(RESULT5_XPATH)
        assert result5.text == result5_text
        sleep(5)

    def test_listBy_date(self):
        self.pre_condition()
        listBar = self.waitForElementVisible(LISTBAR_XPATH)
        listBar.click()
        listByYtoE = self.waitForElementVisible(LISTBYYTOE)
        listByYtoE.click()
        sleep(2)
        result6 = self.waitForElementVisible(RESULT6_XPATH)
        result7 = self.waitForElementVisible(RESULT7_XPATH)
        tarih1 = datetime.strptime(result6.text, "%d.%m.%Y")
        tarih2 = datetime.strptime(result7.text, "%d.%m.%Y")
        assert tarih1 > tarih2
        sleep(2)
        listBar = self.waitForElementVisible(LISTBAR_XPATH)
        listBar.click()
        listByEtoY = self.waitForElementVisible(LISTBYETOY)
        listByEtoY.click()
        sleep(2)
        result8 = self.waitForElementVisible(RESULT8_XPATH)
        result9 = self.waitForElementVisible(RESULT9_XPATH)
        tarih3 = datetime.strptime(result8.text, "%d.%m.%Y")
        tarih4 = datetime.strptime(result9.text, "%d.%m.%Y")
        assert tarih3 < tarih4
        sleep(2) 

    def test_hide_news_and_announcementes(self):
        self.test_success()
        readMore = self.waitForElementVisible(READMORE_XPATH)
        readMore.click()
        sleep(2)
        closePopUp = self.waitForElementVisible(CLOSEPOPUP_CSS)
        closePopUp.click()
        sleep(2)
        hideRead = self.waitForElementVisible(HIDEREAD_XPATH)
        hideRead.click()
        sleep(2)
        result10 = self.waitForElementInvisible(RESULT10_XPATH)
        assert result10 #burası bug o yüzden fail

        #bunun sadece constantları vs düzenlenecek

        






        

        




    








