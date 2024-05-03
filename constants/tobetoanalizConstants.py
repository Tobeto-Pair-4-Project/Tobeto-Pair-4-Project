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
REVIEWSBUTTON_CSS = (By.CSS_SELECTOR, "li:nth-of-type(3) > .c-gray-3.nav-link")
VIEWREPORTBUTTON_CSS = (By.CSS_SELECTOR, ".btn.btn-primary") 
GREENDOT_CSS = (By.CSS_SELECTOR, ".col-12.col-md-7.my-3 > .chartjs-render-monitor")
NEWWORLD_CSS = (By.CSS_SELECTOR, "div#accordionExample > div:nth-of-type(1) .fw-bolder.h6.mb-0.text-primary")
newWorld_text = "Yeni dünyaya hazırlanıyorum"
NEWWORLD1_CSS = (By.CSS_SELECTOR, "#heading8 .fw-bolder")
NEWWORLD2_CSS = (By.CSS_SELECTOR, "#heading28 .fw-bolder")
NEWWORLD3_CSS = (By.CSS_SELECTOR, "#hheading8 .fw-bolder")
PROFESSIONALSTANCE_CSS = (By.CSS_SELECTOR, "div:nth-of-type(5) .fw-bolder.h6.mb-0.text-primary")
professionalStance_text = "Profesyonel duruşumu geliştiriyorum"
PROFESSIONALSTANCE1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(6) > .accordion-header  .fw-bolder")
PROFESSIONALSTANCE2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(7) > .accordion-header  .fw-bolder")
PROFESSIONALSTANCE3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(8) > .accordion-header  .fw-bolder")
IKNOWMYSELF_CSS = (By.CSS_SELECTOR, "div:nth-of-type(9) .fw-bolder.h6.mb-0.text-primary")
iknowMyself_text = "Kendimi tanıyor ve yönetiyorum"
IKNOWMYSELF1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(10) > .accordion-header  .fw-bolder")
IKNOWMYSELF2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(11) > .accordion-header  .fw-bolder")
IKNOWMYSELF3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(12) > .accordion-header  .fw-bolder")
CREATIVESOLUTIONS_CSS = (By.CSS_SELECTOR, "div:nth-of-type(13) .fw-bolder.h6.mb-0.text-primary")
creativeSolutions_text = "Yaratıcı ve doğru çözümler geliştiriyorum"
CREATIVESOLUTIONS1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(14) > .accordion-header  .fw-bolder")
CREATIVESOLUTIONS2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(15) > .accordion-header  .fw-bolder")
CREATIVESOLUTIONS3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(16) > .accordion-header  .fw-bolder")
WORKINGWITHOTHERS_CSS = (By.CSS_SELECTOR, "div:nth-of-type(17) .fw-bolder.h6.mb-0.text-primary")
workingWithOthers_text = "Başkaları ile birlikte çalışıyorum"
WORKINGWITHOTHERS1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(18) > .accordion-header  .fw-bolder")
WORKINGWITHOTHERS2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(19) > .accordion-header  .fw-bolder")
WORKINGWITHOTHERS3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(20) > .accordion-header  .fw-bolder")
SELFIMPROVEMENT_CSS = (By.CSS_SELECTOR, "div:nth-of-type(21) .fw-bolder.h6.mb-0.text-primary")
selfImprovement_text = "Kendimi sürekli geliştiriyorum"
SELFIMPROVEMENT1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(22) > .accordion-header  .fw-bolder")
SELFIMPROVEMENT2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(23) > .accordion-header  .fw-bolder")
SELFIMPROVEMENT3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(24) > .accordion-header  .fw-bolder")
RESULTSORIENTED_CSS = (By.CSS_SELECTOR, "div:nth-of-type(25) .fw-bolder.h6.mb-0.text-primary")
resultsOriented_text = "Sonuç ve başarı odaklıyım"
RESULTSORIENTED1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(26) > .accordion-header  .fw-bolder")
RESULTSORIENTED2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(27) > .accordion-header  .fw-bolder")
RESULTSORIENTED3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(28) > .accordion-header  .fw-bolder")
IUNDERSTAND_CSS = (By.CSS_SELECTOR, "div:nth-of-type(29) .fw-bolder.h6.mb-0.text-primary")
iUnderstand_text = "Anlıyorum ve anlaşılıyorum"
IUNDERSTAND1_CSS = (By.CSS_SELECTOR, "div:nth-of-type(30) > .accordion-header  .fw-bolder")
IUNDERSTAND2_CSS = (By.CSS_SELECTOR, "div:nth-of-type(31) > .accordion-header  .fw-bolder")
IUNDERSTAND3_CSS = (By.CSS_SELECTOR, "div:nth-of-type(32) > .accordion-header  .fw-bolder")
