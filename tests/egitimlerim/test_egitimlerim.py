from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.egitimlerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os

class Test_Egitimlerim:

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
        sleep(2)
        
        lessons = self.waitForElementVisible(LESSONS_ID)
        lessons.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        showMore = self.waitForElementVisible(SHOWMORE_XPATH)
        showMore.click()
        sleep(2)
        selectBox = self.waitForElementVisible(SELECTBOX_XPATH)
        selectBox.click()
        selectIstanbulKodluyor = self.waitForElementVisible(ISTANBULKODLUYOR_ID)
        selectIstanbulKodluyor.click()
        sleep(3)
        
    #TC01 tüm eğitimlerim bölümü
    #a'dan z'ye sıralama  
    def test_tumegitimlerim_list_by_AtoZ(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        #allLessons.click()
        assert allLessons.text == alllessons_text
        sleep(2)
        
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        listByAtoZ = self.waitForElementVisible(LISTBYATOZ_ID)
        listByAtoZ.click()
        sleep(2)
        lesson1 = self.waitForElementVisible(lesson1_xpath)
        lesson2 = self.waitForElementVisible(lesson2_xpath)
        assert lesson1.text < lesson2.text

    #z'den a'ya sıralama
    def test_tumegitimlerimlist_by_ZtoA(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        assert allLessons.text == alllessons_text
        sleep(2)

        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByZtoA = self.waitForElementVisible(LISTBYZTOA_ID)
        listByZtoA.click()
        sleep(2)
        lesson1 = self.waitForElementVisible(lesson1_xpath)
        lesson2 = self.waitForElementVisible(lesson2_xpath)
        assert lesson1.text > lesson2.text

    #yeniden eskiye sıralama
    def test_tumegitimlerim_list_by_newest(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        assert allLessons.text == alllessons_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByYtoE = self.waitForElementVisible(LISTBYYTOE_ID) 
        sleep(3)
        listByYtoE.click()
        sleep(2)
        lesson1 = self.waitForElementVisible(lesson1date_xpath).text
        lesson2 = self.waitForElementVisible(lesson2date_xpath).text

        parts = lesson1.split(" ")
        lesson1 = lesson1.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2.split(" ")
        lesson2 = lesson2.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson1, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson2, "%d %b %Y %H:%M")
        assert date1 > date2

    #eskiden yeniye sıralama
    def test_tumegitimlerim_list_by_oldest(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        assert allLessons.text == alllessons_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByEtoY = self.waitForElementVisible(LISTBYETOY_ID) 
        sleep(3)
        listByEtoY.click()
        sleep(2)

        lesson1 = self.waitForElementVisible(lesson1date_xpath).text
        lesson2 = self.waitForElementVisible(lesson2date_xpath).text

        parts = lesson1.split(" ")
        lesson1 = lesson1.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2.split(" ")
        lesson2 = lesson2.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson1, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson2, "%d %b %Y %H:%M")
        assert date1 < date2
        



    #TC02 devam ettiklerim bölümü
        
    #a'dan z'ye sıralama  
    def test_devamettiklerim_list_by_AtoZ(self):
        self.pre_condition()
        ongoings = self.waitForElementVisible(ONGOINGS_ID)
        ongoings.click()
        assert ongoings.text == ongoings_text
        sleep(2)
        
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        listByAtoZ = self.waitForElementVisible(LISTBYATOZ_ID)
        listByAtoZ.click()
        sleep(2)
        lesson1d = self.waitForElementVisible(lesson1d_xpath)
        lesson2d = self.waitForElementVisible(lesson2d_xpath)
        assert lesson1d.text < lesson2d.text

    #z'den a'ya sıralama
    def test_devamettiklerim_by_ZtoA(self):
        self.pre_condition()
        ongoings = self.waitForElementVisible(ONGOINGS_ID)
        ongoings.click()
        assert ongoings.text == ongoings_text
        sleep(2)

        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()                                          
        sleep(3)
        listByZtoA = self.waitForElementVisible(LISTBYZTOA_ID)
        listByZtoA.click()
        sleep(2)
        lesson1d = self.waitForElementVisible(lesson1d_xpath)
        lesson2d = self.waitForElementVisible(lesson2d_xpath)
        assert lesson1d.text > lesson2d.text

    #yeniden eskiye sıralama
    def test_devamettiklerim_list_by_newest(self):
        self.pre_condition()
        ongoings = self.waitForElementVisible(ONGOINGS_ID)
        ongoings.click()
        assert ongoings.text == ongoings_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByYtoE = self.waitForElementVisible(LISTBYYTOE_ID) 
        sleep(3)
        listByYtoE.click()
        sleep(2)
        lesson1d = self.waitForElementVisible(lesson1ddate_xpath).text
        lesson2d = self.waitForElementVisible(lesson2ddate_xpath).text

        parts = lesson1d.split(" ")
        lesson1d = lesson1d.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2d.split(" ")
        lesson2d = lesson2d.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson1d, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson2d, "%d %b %Y %H:%M")
        assert date1 > date2

    #eskiden yeniye sıralama
    def test_devamettiklerim_list_by_oldest(self):
        self.pre_condition()
        ongoings = self.waitForElementVisible(ONGOINGS_ID)
        ongoings.click()
        assert ongoings.text == ongoings_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByEtoY = self.waitForElementVisible(LISTBYETOY_ID) 
        sleep(3)
        listByEtoY.click()
        sleep(2)

        lesson1d = self.waitForElementVisible(lesson1ddate_xpath).text
        lesson2d= self.waitForElementVisible(lesson2ddate_xpath).text

        parts = lesson1d.split(" ")
        lesson1d = lesson1d.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2d.split(" ")
        lesson2d = lesson2d.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson1d, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson2d, "%d %b %Y %H:%M")
        assert date1 < date2



    #TC03 tamamladıklarım bölümü
    
     #a'dan z'ye sıralama  
    def test_tamamladiklarim_list_by_AtoZ(self):
        self.pre_condition()
        doneLessons = self.waitForElementVisible(DONELESSONS_ID)
        doneLessons.click()
        assert doneLessons.text == doneLessons_text
        sleep(2)
        
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        listByAtoZ = self.waitForElementVisible(LISTBYATOZ_ID)
        listByAtoZ.click()
        sleep(2)
        lesson1t = self.waitForElementVisible(lesson1t_xpath)
        lesson2t = self.waitForElementVisible(lesson2t_xpath)
        assert lesson1t.text < lesson2t.text

    #z'den a'ya sıralama
    def test_tamamladiklarim_by_ZtoA(self):
        self.pre_condition()
        doneLessons = self.waitForElementVisible(DONELESSONS_ID)
        doneLessons.click()
        assert doneLessons.text == doneLessons_text
        sleep(2)

        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()                                          
        sleep(3)
        listByZtoA = self.waitForElementVisible(LISTBYZTOA_ID)
        listByZtoA.click()
        sleep(2)
        lesson1t = self.waitForElementVisible(lesson1t_xpath)
        lesson2t = self.waitForElementVisible(lesson2t_xpath)
        assert lesson1t.text > lesson2t.text

    #yeniden eskiye sıralama
    def test_tamamladiklarim_list_by_newest(self):
        self.pre_condition()
        doneLessons = self.waitForElementVisible(DONELESSONS_ID)
        doneLessons.click()
        assert doneLessons.text == doneLessons_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByYtoE = self.waitForElementVisible(LISTBYYTOE_ID) 
        sleep(3)
        listByYtoE.click()
        sleep(2)
        lesson1t = self.waitForElementVisible(lesson1tdate_xpath).text
        lesson2t = self.waitForElementVisible(lesson2tdate_xpath).text

        parts = lesson1t.split(" ")
        lesson1t = lesson1t.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2t.split(" ")
        lesson2t = lesson2t.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson1t, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson2t, "%d %b %Y %H:%M")
        assert date1 > date2

    #eskiden yeniye sıralama
    def test_tamamladiklarim_list_by_oldest(self):
        self.pre_condition()
        doneLessons = self.waitForElementVisible(DONELESSONS_ID)
        doneLessons.click()
        assert doneLessons.text == doneLessons_text
        listBY = self.waitForElementVisible(LISTBY_CSS)
        listBY.click()
        sleep(3)
        listByEtoY = self.waitForElementVisible(LISTBYETOY_ID) 
        sleep(3)
        listByEtoY.click()
        sleep(2)

        lesson3t = self.waitForElementVisible(lesson3tdate_xpath).text
        lesson4t= self.waitForElementVisible(lesson4tdate_xpath).text

        parts = lesson3t.split(" ")
        lesson3t = lesson3t.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson4t.split(" ")
        lesson4t = lesson4t.replace(parts[1],months_tr[parts[1]])


        date1 = datetime.strptime(lesson3t, "%d %b %Y %H:%M")
        date2 = datetime.strptime(lesson4t, "%d %b %Y %H:%M")
        assert date1 < date2 

    #TC04
    def test_search_lessons(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        assert allLessons.text == alllessons_text
        searcBox = self.waitForElementVisible(SEARCHBOX_ID)
        searcBox.click()
        searcBox.send_keys("İstanbul Kodluyor Proje Aşamaları")
        projectSteps = self.waitForElementVisible(PROJECTSTEPS_XPATH)
        assert projectSteps.text == projectSteps_text

    #TC05
    def test_search_lessons_null(self):
        self.pre_condition()
        allLessons = self.waitForElementVisible(ALLLESSONS_ID)
        assert allLessons.text == alllessons_text
        searcBox = self.waitForElementVisible(SEARCHBOX_ID)
        searcBox.click()
        searcBox.send_keys("Javascript")
        sleep(2)
        noResultAlert = self.waitForElementVisible(NORESULTALERT_XPATH)
        assert noResultAlert.text == noResultAlert_text




        


    

     


   
