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
MYEXPERIENCES_CSS = (By.CSS_SELECTOR,"a:nth-of-type(2) > .sidebar-text")
CORPORATIONNAME_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
POSITION_NAME = (By.NAME, "position")
SECTOR_NAME = (By.NAME, "sector")
CITY_NAME = (By.NAME, "country")
ISTANBULOPTION2_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select/option[41]")
STARTINGDATE_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input")
MONTHDROPDOWN1_CSS = (By.CSS_SELECTOR, ".react-datepicker__month-select")
ARALIKOPTION_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[12]")
YEARDROPDOWN1_CSS = (By.CSS_SELECTOR, ".react-datepicker__year-select")
OPTION2023_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[50]")
DAYOPTION1_CSS = (By.CSS_SELECTOR, ".react-datepicker__day--004:nth-child(4)")
FINISHDATE_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input")
MONTHDROPDOWN2_CSS = (By.CSS_SELECTOR, ".react-datepicker__month-select")
NISANOPTION_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[4]")
DAYOPTION2_CSS = (By.CSS_SELECTOR, ".react-datepicker__day--005:nth-child(5)")
JOBDESCRIPTION_CSS = (By.CSS_SELECTOR, ".col-md-12 > .form-control")
SAVEBUTTON_CSS = (By.CSS_SELECTOR, ".btn-primary")
THREEDOT_CSS = (By.CSS_SELECTOR, ".grade-info")
EXPVERIFIED_XPATH = (By.XPATH, "//body/div[@role='dialog']/div//span[@class='grade-details-header']")
CLOSEBUTTON_XPATH = (By.XPATH, "//body/div[@role='dialog']/div//button[@type='button']")
SAVEVERIFIED_XPATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[1]/span[1]")
REQALERT1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger")
REQALERT2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger")
REQALERT3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger")
REQALERT4_CSS = (By.CSS_SELECTOR, "div:nth-of-type(5) > .text-danger")
REQALERT5_CSS = (By.CSS_SELECTOR, "div:nth-of-type(6) > .text-danger")
REQALERT6_CSS = (By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger")
REQALERT7_CSS = (By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger")
REQALERT8_CSS = (By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger")
REQALERT9_CSS = (By.CSS_SELECTOR, "div:nth-of-type(5) > .text-danger")
REQALERT10_CSS = (By.CSS_SELECTOR, "div:nth-of-type(6) > .text-danger")
REQALERT11_CSS = (By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger")
REQALERT12_CSS = (By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger")
REQALERT13_CSS = (By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger")
REQALERT14_CSS = (By.CSS_SELECTOR, ".col-12.col-md-12.mb-6 > .text-danger")
DELETEFIRSTEXPBUTTON_CSS = (By.CSS_SELECTOR, ".grade-delete")
DELETEALERT_CSS = (By.CSS_SELECTOR, ".alert-message.mx-3")
NOBUTTON_CSS = (By.CSS_SELECTOR, ".btn.btn-no.my-3")
YESBUTTON_CSS = (By.CSS_SELECTOR, ".btn.btn-yes.my-3")
DELETEVERIFIED_CSS = (By.CSS_SELECTOR, "div[role='alert'] > .toast-body")
STILLWORKINGBUTTON_NAME = (By.NAME, "checkbox")
CORPORATION1TEXT = "Tobeto"
CORPORATION2TEXT = "Tobe"
CORPORATION3TEXT = "tobetotobetotobetotobetotobetotobetotobetotobetotobetotobeto"
POSITION1TEXT = "Eğitmen"
POSITION2TEXT = "Eğit"
POSITION3TEXT = "EgitmenEgitmenEgitmenEgitmenEgitmenEgitmenEgitmenEgitmen"
SECTOR1TEXT = "Eğitim"
SECTOR2TEXT = "Eğit"
SECTOR3TEXT = "EgitimegitimEgitimegitimEgitimegitimEgitimegitimEgitimegitim"
JOBDESCRIPTION1TEXT = "Tobeto'da eğitmenlik yaptım"
JOBDESCRIPTION2TEXT = "TobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetoto"
CORPORATIONTEXT = "Kurum Adı"
EXPVERIFIEDTEXT = "İş Açıklaması"
SAVEVERIFIEDTEXT = "Kurum Adı"
REQALERT1TEXT = "Doldurulması zorunlu alan*"
REQALERT2TEXT = "Doldurulması zorunlu alan*"
REQALERT3TEXT = "Doldurulması zorunlu alan*"
REQALERT4TEXT = "Doldurulması zorunlu alan*"
REQALERT5TEXT = "Doldurulması zorunlu alan*"
REQALERT6TEXT = "Doldurulması zorunlu alan*"
REQALERT7TEXT = "Doldurulması zorunlu alan*"
REQALERT8TEXT = "Doldurulması zorunlu alan*"
REQALERT9TEXT = "Doldurulması zorunlu alan*"
REQALERT10TEXT = "Doldurulması zorunlu alan*"
REQALERT11TEXT = "En fazla 50 karakter girebilirsiniz"
REQALERT12TEXT = "En fazla 50 karakter girebilirsiniz"
REQALERT13TEXT = "En fazla 50 karakter girebilirsiniz"
REQALERT14TEXT = "En fazla 300 karakter girebilirsiniz"
DELETEALERTTEXT = "Seçilen deneyimi silmek istediğinize emin misiniz ?"
DELETEVERIFIEDTEXT = "• Deneyim kaldırıldı."



