from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.tobetoanalizConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os


class Test_TobetoAnaliz:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
    
    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=15):
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
        reviewsButton = self.waitForElementVisible(REVIEWSBUTTON_CSS)
        reviewsButton.click()

    def test_view_report(self):
        self.pre_condition()
        actions3 = ActionChains(self.driver)
        viewReportButton = self.waitForElementClickable(VIEWREPORTBUTTON_CSS)
        viewReportButton.click()
        greenDot = self.waitForElementVisible(GREENDOT_CSS)
        actions3.move_to_element(greenDot).perform()
        
        #yeni dünyaya hazırlanıyorum bölümü
        newWorld = self.waitForElementVisible(NEWWORLD_CSS)
        assert newWorld.text == newWorld_text
        
        newWorld1 = self.waitForElementVisible(NEWWORLD1_CSS)
        actions3.double_click(newWorld1).perform()
        sleep(2)
        
        newWorld2 = self.waitForElementVisible(NEWWORLD2_CSS)
        actions3.click(newWorld2).perform()
        sleep(2)
        
        newWorld3 = self.waitForElementVisible(NEWWORLD3_CSS)
        actions3.double_click(newWorld3).perform()
        sleep(2)
        

        #profesyonel duruşumu geliştiriyorum bölümü
        professionalStance = self.waitForElementVisible(PROFESSIONALSTANCE_CSS)
        assert professionalStance.text == professionalStance_text
        
        professionalStance1 = self.waitForElementVisible(PROFESSIONALSTANCE1_CSS)
        actions3.double_click(professionalStance1).perform()
        sleep(2)
        
        professionalStance2 = self.waitForElementVisible(PROFESSIONALSTANCE2_CSS)
        actions3.double_click(professionalStance2).perform()
        sleep(2)
        
        professionalStance3 = self.waitForElementVisible(PROFESSIONALSTANCE3_CSS)
        actions3.double_click(professionalStance3).perform()
        sleep(2)
        

        #kendimi tanıyor ve yönetiyorum bölümü
        iknowMyself = self.waitForElementVisible(IKNOWMYSELF_CSS)
        assert iknowMyself.text == iknowMyself_text
        
        iknowMyself1 = self.waitForElementVisible(IKNOWMYSELF1_CSS)
        actions3.double_click(iknowMyself1).perform()
        sleep(2)
        
        iknowMyself2 = self.waitForElementVisible(IKNOWMYSELF2_CSS)
        actions3.double_click(iknowMyself2).perform()
        sleep(2)
        
        iknowMyself3 = self.waitForElementVisible(IKNOWMYSELF3_CSS)
        actions3.double_click(iknowMyself3).perform()
        sleep(2)


        #yaratıcı ve doğru çözümler geliştiriyorum bölümü
        creativerSolutions = self.waitForElementVisible(CREATIVESOLUTIONS_CSS)
        assert creativerSolutions.text == creativeSolutions_text

        creativerSolutions1 = self.waitForElementVisible(CREATIVESOLUTIONS1_CSS)
        actions3.double_click(creativerSolutions1).perform()
        sleep(2)

        creativerSolutions2 = self.waitForElementVisible(CREATIVESOLUTIONS2_CSS)
        actions3.double_click(creativerSolutions2).perform()
        sleep(2)

        creativerSolutions3 = self.waitForElementVisible(CREATIVESOLUTIONS3_CSS)
        actions3.double_click(creativerSolutions3).perform()
        sleep(2)

        #Başkaları ile birlikte çalışıyorum bölümü
        workingWithOthers = self.waitForElementVisible(WORKINGWITHOTHERS_CSS)
        assert workingWithOthers.text == workingWithOthers_text

        workingWithOthers1 = self.waitForElementVisible(WORKINGWITHOTHERS1_CSS)
        actions3.double_click(workingWithOthers1).perform()
        sleep(2)

        workingWithOthers2 = self.waitForElementVisible(WORKINGWITHOTHERS2_CSS)
        actions3.double_click(workingWithOthers2).perform()
        sleep(2)

        workingWithOthers3 = self.waitForElementVisible(WORKINGWITHOTHERS3_CSS)
        actions3.double_click(workingWithOthers3).perform()
        sleep(2)


        #kendimi sürekli geliştiriyorum bölümü
        selfImprovement = self.waitForElementVisible(SELFIMPROVEMENT_CSS)
        assert selfImprovement.text == selfImprovement_text

        selfImprovement1 = self.waitForElementVisible(SELFIMPROVEMENT1_CSS)
        actions3.double_click(selfImprovement1).perform()
        sleep(2)

        selfImprovement2 = self.waitForElementVisible(SELFIMPROVEMENT2_CSS)
        actions3.double_click(selfImprovement2).perform()
        sleep(2)

        selfImprovement3 = self.waitForElementVisible(SELFIMPROVEMENT3_CSS)
        actions3.double_click(selfImprovement3).perform()
        sleep(2)


        #sonuç ve başarı odaklıyım bölümü
        resultsOriented = self.waitForElementVisible(RESULTSORIENTED_CSS)
        assert resultsOriented.text == resultsOriented_text

        resultsOriented1 = self.waitForElementVisible(RESULTSORIENTED1_CSS)
        actions3.double_click(resultsOriented1).perform()
        sleep(2)

        resultsOriented2 = self.waitForElementVisible(RESULTSORIENTED2_CSS)
        actions3.double_click(resultsOriented2).perform()
        sleep(2)

        resultsOriented3 = self.waitForElementVisible(RESULTSORIENTED3_CSS)
        actions3.double_click(resultsOriented3).perform()
        sleep(2)


        #anlıyorum ve anlaşılıyorum bölümü
        iUnderstand = self.waitForElementVisible(IUNDERSTAND_CSS)
        assert iUnderstand.text == iUnderstand_text

        iUnderstand1 = self.waitForElementVisible(IUNDERSTAND1_CSS)
        actions3.double_click(iUnderstand1).perform()
        sleep(2)

        iUnderstand2 = self.waitForElementVisible(IUNDERSTAND2_CSS)
        actions3.double_click(iUnderstand2).perform()
        sleep(2)

        iUnderstand3 = self.waitForElementVisible(IUNDERSTAND3_CSS)
        actions3.double_click(iUnderstand3).perform()
        sleep(2)
