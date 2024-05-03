from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.deneyimlerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os

class Test_Deneyimlerim:
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
        profileButton = self.waitForElementVisible(PROFILEBUTTON_XPATH)
        profileButton.click()
        profileInfo = self.waitForElementVisible(PROFILEINFO_XPATH)
        profileInfo.click()
        myExperiences = self.waitForElementVisible(MYEXPERIENCES_CSS)
        myExperiences.click()

    
    def test_adding_experiment(self):
        self.pre_condition()
        corporationName = self.waitForElementVisible(CORPORATIONNAME_XPATH)
        corporationName.click()
        corporationName.send_keys(CORPORATION1TEXT)
        position = self.waitForElementVisible(POSITION_NAME)
        position.click()
        position.send_keys(POSITION1TEXT)
        sector = self.waitForElementVisible(SECTOR_NAME)
        sector.click()
        sector.send_keys(SECTOR1TEXT)
        city = self.waitForElementVisible(CITY_NAME)
        city.click()
        istanbulOption2 = self.waitForElementVisible(ISTANBULOPTION2_XPATH)
        istanbulOption2.click()
        city.click()
        startingDate = self.waitForElementClickable(STARTINGDATE_XPATH)
        
        startingDate.click()
        monthDropdown1 = self.waitForElementVisible(MONTHDROPDOWN1_CSS) 
        monthDropdown1.click()
        aralikOption = self.waitForElementVisible(ARALIKOPTION_XPATH)
        aralikOption.click()
        yearDropdown1 = self.waitForElementVisible(YEARDROPDOWN1_CSS)
        yearDropdown1.click()
        option2023 = self.waitForElementVisible(OPTION2023_XPATH)
        option2023.click()
        dayOption1 = self.waitForElementVisible(DAYOPTION1_CSS)
        dayOption1.click()
        finishDate = self.waitForElementClickable(FINISHDATE_XPATH)

        finishDate.click()
        monthDropdown2 = self.waitForElementVisible(MONTHDROPDOWN2_CSS) 
        monthDropdown2.click()
        nisanOption = self.waitForElementVisible(NISANOPTION_XPATH)
        nisanOption.click()
        dayOption2 = self.waitForElementVisible(DAYOPTION2_CSS)
        dayOption2.click()  
        jobDescription = self.waitForElementVisible(JOBDESCRIPTION_CSS)
        jobDescription.click()
        jobDescription.send_keys(JOBDESCRIPTION1TEXT)
        saveButton = self.waitForElementVisible(SAVEBUTTON_CSS)
        saveButton.click()
        sleep(2)
        threeDot =self.waitForElementClickable(THREEDOT_CSS)
        threeDot.click()
        expVerified = self.waitForElementVisible(EXPVERIFIED_XPATH)
        assert expVerified.text == EXPVERIFIEDTEXT
        closeButton = self.waitForElementClickable(CLOSEBUTTON_XPATH)
        saveVerified = self.waitForElementVisible(SAVEVERIFIED_XPATH)
        assert saveVerified.text == SAVEVERIFIEDTEXT
        sleep(2)

    def test_add_experiment_without_interaction(self):
        self.pre_condition()
        saveButton = self.waitForElementVisible(SAVEBUTTON_CSS)
        saveButton.click()
        sleep(2)
        reqAlert1 = self.waitForElementVisible(REQALERT1_CSS)
        reqAlert2 = self.waitForElementVisible(REQALERT2_CSS)
        reqAlert3 = self.waitForElementVisible(REQALERT3_CSS)
        reqAlert4 = self.waitForElementVisible(REQALERT4_CSS)
        reqAlert5 = self.waitForElementVisible(REQALERT5_CSS)
        assert {reqAlert1.text == REQALERT1TEXT,
                    reqAlert2.text == REQALERT2TEXT,
                    reqAlert3.text == REQALERT3TEXT,
                    reqAlert4.text == REQALERT4TEXT,
                    reqAlert5.text == REQALERT5TEXT}
        
    def test_experiment_while_working(self):
        self.pre_condition()
        corporationName = self.waitForElementVisible(CORPORATIONNAME_XPATH)
        corporationName.click()
        corporationName.send_keys(CORPORATION1TEXT)
        position = self.waitForElementVisible(POSITION_NAME)
        position.click()
        position.send_keys(POSITION1TEXT)
        sector = self.waitForElementVisible(SECTOR_NAME)
        sector.click()
        sector.send_keys(SECTOR1TEXT)
        city = self.waitForElementVisible(CITY_NAME)
        city.click()
        istanbulOption2 = self.waitForElementVisible(ISTANBULOPTION2_XPATH)
        istanbulOption2.click()
        city.click()
        startingDate = self.waitForElementClickable(STARTINGDATE_XPATH)
        
        startingDate.click()
        monthDropdown1 = self.waitForElementVisible(MONTHDROPDOWN1_CSS) 
        monthDropdown1.click()
        aralikOption = self.waitForElementVisible(ARALIKOPTION_XPATH)
        aralikOption.click()
        yearDropdown1 = self.waitForElementVisible(YEARDROPDOWN1_CSS)
        yearDropdown1.click()
        option2023 = self.waitForElementVisible(OPTION2023_XPATH)
        option2023.click()
        dayOption1 = self.waitForElementVisible(DAYOPTION1_CSS)
        dayOption1.click()
        finishDate = self.waitForElementClickable(FINISHDATE_XPATH)

        stillWorkingButton = self.waitForElementClickable(STILLWORKINGBUTTON_NAME)
        stillWorkingButton.click()
        assert not finishDate.is_enabled()
        saveButton = self.waitForElementVisible(SAVEBUTTON_CSS)
        saveButton.click()
        sleep(2)
        threeDot =self.waitForElementClickable(THREEDOT_CSS)
        threeDot.click()
        expVerified = self.waitForElementVisible(EXPVERIFIED_XPATH)
        assert expVerified.text == EXPVERIFIEDTEXT
        closeButton = self.waitForElementClickable(CLOSEBUTTON_XPATH)
        saveVerified = self.waitForElementVisible(SAVEVERIFIED_XPATH)
        assert saveVerified.text == SAVEVERIFIEDTEXT

    def test_min_character(self):
        self.pre_condition()
        corporationName = self.waitForElementVisible(CORPORATIONNAME_XPATH)
        corporationName.click()
        corporationName.send_keys(CORPORATION2TEXT)
        position = self.waitForElementVisible(POSITION_NAME)
        position.click()
        position.send_keys(POSITION2TEXT)
        sector = self.waitForElementVisible(SECTOR_NAME)
        sector.click()
        sector.send_keys(SECTOR2TEXT)
        saveButton = self.waitForElementVisible(SAVEBUTTON_CSS)
        saveButton.click()
        sleep(2)
        reqAlert6 = self.waitForElementVisible(REQALERT6_CSS)
        reqAlert7 = self.waitForElementVisible(REQALERT7_CSS)
        reqAlert8 = self.waitForElementVisible(REQALERT8_CSS)
        reqAlert9 = self.waitForElementVisible(REQALERT9_CSS)
        reqAlert10 = self.waitForElementVisible(REQALERT10_CSS)
        assert {reqAlert6.text == REQALERT6TEXT,
                    reqAlert7.text == REQALERT7TEXT,
                    reqAlert8.text == REQALERT8TEXT,
                    reqAlert9.text == REQALERT9TEXT,
                    reqAlert10.text == REQALERT10TEXT}
        
    
    def test_max_character(self):
        self.pre_condition()
        corporationName = self.waitForElementVisible(CORPORATIONNAME_XPATH)
        corporationName.click()
        corporationName.send_keys(CORPORATION3TEXT)
        position = self.waitForElementVisible(POSITION_NAME)
        position.click()
        position.send_keys(POSITION3TEXT)
        sector = self.waitForElementVisible(SECTOR_NAME)
        sector.click()
        sector.send_keys(SECTOR3TEXT)
        jobDescription = self.waitForElementVisible(JOBDESCRIPTION_CSS)
        jobDescription.click()
        jobDescription.send_keys(JOBDESCRIPTION2TEXT)
        saveButton = self.waitForElementVisible(SAVEBUTTON_CSS)
        saveButton.click()
        sleep(2)
        reqAlert11 = self.waitForElementVisible(REQALERT11_CSS)
        reqAlert12 = self.waitForElementVisible(REQALERT12_CSS)
        reqAlert13 = self.waitForElementVisible(REQALERT13_CSS)
        reqAlert14 = self.waitForElementVisible(REQALERT14_CSS)
        assert {reqAlert11.text == REQALERT11TEXT,
                    reqAlert12.text == REQALERT12TEXT,
                    reqAlert13.text == REQALERT13TEXT,
                    reqAlert14.text == REQALERT14TEXT}
        

    def test_delete_experiment(self):
        self.pre_condition()
        deleteFirstExperimentButton = self.waitForElementClickable(DELETEFIRSTEXPBUTTON_CSS)
        deleteFirstExperimentButton.click()
        deleteAlert = self.waitForElementVisible(DELETEALERT_CSS)
        assert deleteAlert.text == DELETEALERTTEXT
        noButton = self.waitForElementClickable(NOBUTTON_CSS)
        noButton.click()
        saveVerified = self.waitForElementVisible(SAVEVERIFIED_XPATH)
        assert saveVerified.text == SAVEVERIFIEDTEXT
        deleteFirstExperimentButton.click()
        yesButton = self.waitForElementClickable(YESBUTTON_CSS)
        yesButton.click()
        sleep(2)
        deleteVerified = self.waitForElementVisible(DELETEVERIFIED_CSS)
        assert deleteVerified.text == DELETEVERIFIEDTEXT
        
