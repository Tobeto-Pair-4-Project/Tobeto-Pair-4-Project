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
ANNOUNCEMENTS_XPATH = (By.XPATH, "/html//button[@id='notification-tab']")
SHOWMOREBUTTON_CSS = (By.CSS_SELECTOR, "div#notification-tab-pane  .showMoreBtn")
SEARCHBAR_CSS = (By.CSS_SELECTOR, ".search-box.searchBox")
TYPEBAR_XPATH = (By.XPATH,"(//button[@type='button'])[4]")
LISTBAR_XPATH = (By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div/div[4]/div[1]/button[@type='button']")
LISTBYYTOE = (By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//ul[@class='dropdown-menu new-filter show']//a[.='Tarihe Göre (Y-E)']")
LISTBYETOY = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//ul[@class='dropdown-menu new-filter show']//a[.='Tarihe Göre (E-Y)']")

RESULT1_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[1]/div[@class='notfy-card notify']/div[@class='d-flex flex-column']/span[.='Yeni Gelenler için Bilgilendirme']")
result1_text = "Yeni Gelenler için Bilgilendirme"

RESULT2_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[2]/div[@class='notfy-card notify']//span[.='Yeni Gelenler için Bilgilendirme']")
result2_text = "Yeni Gelenler için Bilgilendirme"

RESULT3_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[3]/div[@class='notfy-card notify']//span[.='Yeni Gelenler için Bilgilendirme']")
result3_text = "Yeni Gelenler için Bilgilendirme"

RESULT4_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//p[.='Bir duyuru bulunmamaktadır.']")
result4_text = "Bir duyuru bulunmamaktadır."

OPTION1_ID = (By.ID, "typeNews")
OPTION2_ID = (By.ID, "typeAnnouncement")
SELECTEDPAGE1_CSS = (By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='button']")
selectedpage1_text = "1"
LISTOFRESULTS_CSS = (By.CSS_SELECTOR, "div[class='col-md-4 col-12 my-4']")

RESULT5_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//p[.='Bir duyuru bulunmamaktadır.']")
result5_text = "Bir duyuru bulunmamaktadır."

RESULT6_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]")
RESULT7_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[2]/div/div[2]/span[1]")
RESULT8_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]")
RESULT9_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[2]/div/div[2]/span[1]")
RESULT10_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[1]/span")

READMORE_XPATH = (By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[2]")
CLOSEPOPUP_CSS = (By.CSS_SELECTOR, "div[role='dialog'] .btn-close")
HIDEREAD_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//button[@class='read-hide']")




