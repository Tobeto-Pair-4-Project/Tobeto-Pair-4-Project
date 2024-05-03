from selenium.webdriver.common.by import By

BASE_URL = "https://tobeto.com/giris"
USER_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']")
PASSWORD_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']")
LOGINBUTTON_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']")
userName = "recepkizil7834@gmail.com"
password = "Recep732."
login_verified_text = "• Giriş başarılı."
LOGINVERIFIED_CSS = (By.CSS_SELECTOR,"div[role='alert'] > .toast-body")
CLOSELOGINVERIFIED_CSS = (By.CSS_SELECTOR, ".btn-close:nth-child(3)")

LESSONS_ID = (By.ID, "lessons-tab")
SHOWMORE_XPATH = (By.XPATH, "//div[@class='showMoreBtn']")
SEARCHBOX_ID = (By.ID, "search")
SELECTBOX_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[@class='filter-section mt-3']/div/div[2]/div/div[1]/div[1]/div[2]")
ISTANBULKODLUYOR_ID = (By.ID, "react-select-2-listbox")

#tüm eğitimlerim bölümü
ALLLESSONS_ID = (By.ID, "all-lessons-tab")
alllessons_text = "Tüm Eğitimlerim"

LISTBY_CSS = (By.CSS_SELECTOR, ".css-hlgwow.select__value-container.select__value-container--has-value > .css-19bb58m.select__input-container")
LISTBYATOZ_ID = (By.ID, "react-select-3-option-0")
LISTBYZTOA_ID = (By.ID, "react-select-3-option-1")
LISTBYYTOE_ID = (By.ID, "react-select-3-option-2")
LISTBYETOY_ID = (By.ID, "react-select-3-option-3")


lesson1_xpath = (By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")
lesson2_xpath = (By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[1]")

lesson1date_xpath=(By.XPATH,"//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[2]")
lesson2date_xpath=(By.XPATH,"//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[2]")

months_tr = {
  "Ocak": "Jan",
  "Şubat": "Feb",
  "Mart": "Mar",
  "Nisan": "Apr",
  "Mayıs": "May",
  "Haziran": "Jun",
  "Temmuz": "Jul",
  "Ağustos": "Aug",
  "Eylül": "Sep",
  "Ekim": "Oct",
  "Kasım": "Nov",
  "Aralık": "Dec",
}
PROJECTSTEPS_XPATH = (By.XPATH, "/html//div[@id='all-lessons-tab-pane']/div[@class='row']//span[.='İstanbul Kodluyor Proje Aşamaları']")
projectSteps_text = "İstanbul Kodluyor Proje Aşamaları"
NORESULTALERT_XPATH = (By.XPATH, "//div[@id='all-lessons-tab-pane']//p[.='Size atanan herhangi bir eğitim bulunmamaktadır.']")
noResultAlert_text = "Size atanan herhangi bir eğitim bulunmamaktadır."


#devam ettiklerim bölümü
ONGOINGS_ID = (By.ID, "started-tab")
ongoings_text = "Devam Ettiklerim"

lesson1d_xpath = (By.XPATH,"//*[@id='started-tab-pane']/div/div[1]/div/div[2]/div/span[1]")
lesson2d_xpath = (By.XPATH,"//*[@id='started-tab-pane']/div/div[2]/div/div[2]/div/span[1]")

lesson1ddate_xpath = (By.XPATH,"//*[@id='started-tab-pane']/div/div[1]/div/div[2]/div/span[2]")
lesson2ddate_xpath = (By.XPATH,"//*[@id='started-tab-pane']/div/div[2]/div/div[2]/div/span[2]")



#tamamladıklarım bölümü
DONELESSONS_ID = (By.ID, "done-lessons-tab")
doneLessons_text = "Tamamladıklarım"


lesson1t_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")
lesson2t_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[1]")

lesson1tdate_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[2]")
lesson2tdate_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[2]")

lesson3tdate_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[3]/div/div[2]/div/span[2]")
lesson4tdate_xpath = (By.XPATH, "//*[@id='done-lessons-tab-pane']/div/div[4]/div/div[2]/div/span[2]")


