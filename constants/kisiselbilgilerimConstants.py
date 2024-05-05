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
PROFILEBUTTON_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='back-white']/nav//div[@class='btn-group header-avatar']/button[@type='button']//p[@class='mb-0 name']")
PROFILEINFO_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='back-white']/nav//div[@class='btn-group header-avatar']/ul/li[1]/a[@href='#']")
PROFILEINFOVERIFIED_CSS = (By.CSS_SELECTOR, "a:nth-of-type(1) > .sidebar-text")
profileInfoVerified_text = "Kişisel Bilgilerim"
NAME_NAME = (By.NAME,"name")
YOURSURNAME_NAME = (By.NAME,"surname")
YOURPHONENUMBER_NAME = (By.NAME, "phoneNumber")
YOURBIRTHDATE_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input")
YOURTCNO_NAME = (By.NAME, "identifier")
YOUREMAIL_NAME = (By.NAME, "email")
YOURCOUNTRY_NAME = (By.NAME, "country")
YOURCITYDROPDOWN_NAME = (By.NAME, "city")
ISTANBULOPTION_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[41]")
YOURDISTRICT_NAME = (By.NAME, "district")
PENDIKOPTION_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select/option[29]")
SELECTCITY_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[1]")

SAVEBUTTON_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
YOURSTREET_NAME = (By.NAME, "address")
streetmaxlimit_text = "BatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneş"
YOURSTREETALERT_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']/div/div[11]/span[@class='text-danger']")
yourStreetAlert_text = "En fazla 200 karakter girebilirsiniz"

ABOUTME_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea")
aboutmemaxlimit_text = "Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl."
ABOUTMEALERT_XPATH = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']/div/div[12]/span[@class='text-danger']")
aboutMeAlert_text = "En fazla 300 karakter girebilirsiniz"
PROFILEINFOSAVEDALERT_CSS = (By.CSS_SELECTOR, "div[role='alert'] > .toast-body")
profileInfoSavedAlert_text = "• Bilgileriniz başarıyla güncellendi."
YOURTCNOVERIFIED_CSS = (By.CSS_SELECTOR, "div[role='alert'] > .toast-body")
yourTCnoVerified_text = "• Bilgileriniz başarıyla güncellendi."
EDITBUTTON_XPATH = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//div[@class='col-12 mb-6 text-center']/div[1]/div[1]")
ADDFILE_CSS = (By.CSS_SELECTOR, ".uppy-c-btn")
file_path = "C:\\Users\\recep\\Downloads\\profilephoto.jpg"
file2_path = "C:\\Users\\recep\\Downloads\\image.webp"
UPLOADFILEBUTTON_XPATH = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//div[@class='uppy-Root']/div/div[@role='dialog']//div[@class='uppy-Dashboard-progressindicators']/div[1]//button[@type='button']")
DELETEBUTTON_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[2]")
AREYOUSURE_CSS = (By.CSS_SELECTOR, "div[role='dialog'] p")
areYouSure_text = "Profil fotoğrafını kaldırmak istediğinize emin misiniz ?"
NOBUTTON_CSS = (By.CSS_SELECTOR, ".modal-footer > .btn:nth-child(2)")
YESBUTTON_CSS = (By.CSS_SELECTOR, ".btn-primary:nth-child(1)")
PPREMOVEVERIFIED_CSS = (By.CSS_SELECTOR, "div[role='alert'] > .toast-body")
ppRemoveVerified_text = "• Dosya kaldırma işlemi başarılı."

REQUIREDALERT1_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/span")
REQUIREDALERT2_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[1]")
REQUIREDALERT3_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span")
REQUIREDALERT4_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/span")
REQUIREDALERT5_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/span")
REQUIREDALERT6_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[1]")
REQUIREDALERT7_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]")
REQUIREDALERT8_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]")
INCOMPATIBLEALERT_CSS = (By.CSS_SELECTOR, ".uppy-Informer-animated > p")

requiredAlert1_text = "Doldurulması zorunlu alan*"
requiredAlert2_text = "*Aboneliklerde fatura için doldurulması zorunlu alan"
requiredAlert3_text = "Doldurulması zorunlu alan*"
requiredAlert4_text = "Doldurulması zorunlu alan*"
requiredAlert5_text = "Doldurulması zorunlu alan*"
requiredAlert6_text = "*Aboneliklerde fatura için doldurulması zorunlu alan"
requiredAlert7_text = "TC Kimlik Numarası 11 Haneden Az olamaz"
requiredAlert8_text = "TC Kimlik Numarası 11 Haneden Fazla olamaz"
incompatibleAlert_text = "Sadece image/jpeg, image/png yükleyebilirsiniz"









