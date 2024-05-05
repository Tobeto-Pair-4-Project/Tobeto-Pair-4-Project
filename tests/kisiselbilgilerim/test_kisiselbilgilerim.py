from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.kisiselbilgilerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os
import keyboard

class Test_KisiselBilgilerim:
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
        profileInfoVerified = self.waitForElementVisible(PROFILEINFOVERIFIED_CSS)
        assert profileInfoVerified.text == profileInfoVerified_text

    def test_edit_personal_info(self):
        self.pre_condition()
        sleep(2)
        yourName = self.waitForElementVisible(NAME_NAME, 15)
        yourName.click()
        yourName.clear()
        yourName.send_keys("Recep")
        sleep(2)
        yourSurname = self.waitForElementVisible(YOURSURNAME_NAME,15)
        yourSurname.click()
        yourSurname.clear()
        yourSurname.send_keys("Kızıl")
        sleep(2)
        yourPhoneNumber = self.waitForElementVisible(YOURPHONENUMBER_NAME,15)
        yourPhoneNumber.click()
        yourPhoneNumber.send_keys(Keys.CONTROL + "a")
        yourPhoneNumber.send_keys(Keys.DELETE)
        yourPhoneNumber.send_keys("5360731162")
        sleep(2)
        yourBirthDate = self.waitForElementVisible(YOURBIRTHDATE_XPATH,15)
        yourBirthDate.click()
        yourBirthDate.send_keys(Keys.CONTROL + "a")
        yourBirthDate.send_keys(Keys.DELETE)
        yourBirthDate.send_keys("01.10.2000")
        sleep(2)
        yourTCno = self.waitForElementVisible(YOURTCNO_NAME)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        yourTCno.send_keys("53767727284")
        sleep(2)
        yourEmail = self.waitForElementVisible(YOUREMAIL_NAME)
        assert not yourEmail.is_enabled() #TC kısmının tıklanabilir olmadığının kontrolü
        sleep(2)
        yourCountry = self.waitForElementVisible(YOURCOUNTRY_NAME)
        yourCountry.click()
        yourCountry.send_keys(Keys.CONTROL + "a")
        yourCountry.send_keys(Keys.DELETE)
        yourCountry.send_keys("Türkiye")
        sleep(2)
        yourCitydropdown = self.waitForElementVisible(YOURCITYDROPDOWN_NAME)
        yourCitydropdown.click()
        istanbulOption = self.waitForElementPresent(ISTANBULOPTION_XPATH, 15)
        istanbulOption.click()
        sleep(2)
        yourDistrict = self.waitForElementVisible(YOURDISTRICT_NAME)
        yourDistrict.click()
        pendikOption = self.waitForElementPresent(PENDIKOPTION_XPATH)
        pendikOption.click()
        sleep(4)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(4)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        yourStreet = self.waitForElementVisible(YOURSTREET_NAME)
        yourStreet.click()
        yourStreet.send_keys(Keys.CONTROL + "a")
        yourStreet.send_keys(Keys.DELETE)
        yourStreet.send_keys(streetmaxlimit_text)
        saveButton.click()
        sleep(2)
        yourStreetAlert = self.waitForElementVisible(YOURSTREETALERT_XPATH)
        assert yourStreetAlert.text == yourStreetAlert_text
        sleep(2)
        yourStreet.click()
        yourStreet.send_keys(Keys.CONTROL + "a")
        yourStreet.send_keys(Keys.DELETE)
        yourStreet.send_keys("BatıMahallesi")
        sleep(2)

        aboutMe = self.waitForElementVisible(ABOUTME_XPATH)
        aboutMe.click()
        aboutMe.send_keys(Keys.CONTROL + "a")
        aboutMe.send_keys(Keys.DELETE)
        aboutMe.send_keys(aboutmemaxlimit_text)
        saveButton.click()
        sleep(2)
        aboutMeAlert = self.waitForElementVisible(ABOUTMEALERT_XPATH)
        assert aboutMeAlert.text == aboutMeAlert_text
        sleep(2)
        
        aboutMe.click()
        aboutMe.send_keys(Keys.CONTROL + "a")
        aboutMe.send_keys(Keys.DELETE)
        aboutMe.send_keys("Merhaba, ben Recep Kızıl")
        sleep(2)
        saveButton.click()
        sleep(2)
        profileInfoSavedAlert = self.waitForElementVisible(PROFILEINFOSAVEDALERT_CSS)
        assert profileInfoSavedAlert.text == profileInfoSavedAlert_text
        sleep(2)


    def test_required_fields_empty(self):
        self.pre_condition()
        yourBirthDate = self.waitForElementVisible(YOURBIRTHDATE_XPATH,15)
        yourBirthDate.click()
        yourBirthDate.send_keys(Keys.CONTROL + "a")
        yourBirthDate.send_keys(Keys.DELETE)
        sleep(2)
        yourTCno = self.waitForElementVisible(YOURTCNO_NAME)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        yourCountry = self.waitForElementVisible(YOURCOUNTRY_NAME)
        yourCountry.click()
        yourCountry.send_keys(Keys.CONTROL + "a")
        yourCountry.send_keys(Keys.DELETE)
        sleep(2)
        yourCitydropdown = self.waitForElementVisible(YOURCITYDROPDOWN_NAME)
        yourCitydropdown.click()
        selectCity = self.waitForElementVisible(SELECTCITY_XPATH)
        selectCity.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        sleep(2)
        requiredAlert1 = self.waitForElementVisible(REQUIREDALERT1_XPATH)
        requiredAlert2 = self.waitForElementVisible(REQUIREDALERT2_XPATH)
        requiredAlert3 = self.waitForElementVisible(REQUIREDALERT3_XPATH)
        requiredAlert4 = self.waitForElementVisible(REQUIREDALERT4_XPATH)
        requiredAlert5 = self.waitForElementVisible(REQUIREDALERT5_XPATH)
        assert requiredAlert1.text == requiredAlert1_text
        assert requiredAlert2.text == requiredAlert2_text
        assert requiredAlert3.text == requiredAlert3_text
        assert requiredAlert4.text == requiredAlert4_text
        assert requiredAlert5.text == requiredAlert5_text
        
    def test_edit_yourTCno(self):
        self.pre_condition()
        yourTCno = self.waitForElementVisible(YOURTCNO_NAME)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        sleep(2)
        requiredAlert6 = self.waitForElementVisible(REQUIREDALERT6_XPATH)
        assert requiredAlert6.text == requiredAlert6_text
        sleep(2)
        yourTCno = self.waitForElementVisible(YOURTCNO_NAME)
        yourTCno.click()
        yourTCno.send_keys("123456")
        sleep(2)
        requiredAlert7 = self.waitForElementVisible(REQUIREDALERT7_XPATH)
        assert requiredAlert7.text == requiredAlert7_text
        sleep(2)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        yourTCno.send_keys("123456789101112")
        sleep(2)
        requiredAlert8 = self.waitForElementVisible(REQUIREDALERT8_XPATH)
        assert requiredAlert8.text == requiredAlert8_text
        sleep(2)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        yourTCno.send_keys("53767727284")
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        sleep(2)
        yourTCnoVerified = self.waitForElementVisible(YOURTCNOVERIFIED_CSS)
        assert yourTCnoVerified.text == yourTCnoVerified_text
        sleep(2)

    def test_add_pp_browse(self): #gözat ile profil resmi yükleme
        self.pre_condition()
        editButton = self.waitForElementVisible(EDITBUTTON_XPATH)
        editButton.click()
        sleep(2)
        addFile = self.waitForElementClickable(ADDFILE_CSS)
        addFile.click()
        keyboard.write(file_path)
        keyboard.press("enter")
        uploadFileButton=self.waitForElementVisible(UPLOADFILEBUTTON_XPATH)
        uploadFileButton.click()
        sleep(5)

    def test_add_incompatible_pp(self):
        self.pre_condition()
        edit_button = self.waitForElementVisible(EDITBUTTON_XPATH)
        edit_button.click()
        sleep(2)
        addFile = self.waitForElementClickable(ADDFILE_CSS)
        addFile.click()
        keyboard.write(file2_path)
        keyboard.press("enter")
        incompatibleAlert = self.waitForElementVisible(INCOMPATIBLEALERT_CSS)
        sleep(1)
        assert incompatibleAlert.text == incompatibleAlert_text
        sleep(2)


    def test_delete_pp(self):
        self.pre_condition()
        deleteButton = self.waitForElementVisible(DELETEBUTTON_XPATH)
        deleteButton.click()
        sleep(2)
        areYouSure = self.waitForElementVisible(AREYOUSURE_CSS)
        assert areYouSure.text == areYouSure_text
        sleep(2)
        noButton = self.waitForElementVisible(NOBUTTON_CSS)
        noButton.click()
        sleep(2)
        deleteButton.click()
        sleep(2)
        yesButton = self.waitForElementVisible(YESBUTTON_CSS)
        yesButton.click()
        sleep(2)
        ppRemoveVerified = self.waitForElementVisible(PPREMOVEVERIFIED_CSS)
        assert ppRemoveVerified.text == ppRemoveVerified_text
        sleep(2)

    
        
        
      
        

        


        