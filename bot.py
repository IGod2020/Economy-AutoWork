from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
from datetime import datetime

acc = open("acc.txt", "r")
a = acc.read()
b = a.split(":")

gmail = b[0]
password = b[1]


warnings.filterwarnings("ignore")
options =  webdriver.ChromeOptions()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument('--log-level=3')
#options.add_argument('headless')



driver_path = 'C:\\Users\\Windows\\Documents\\Economy-AutoWork-main\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get('https://discord.com/channels/750887184533553153/939000588799201301')

def comando():
    if '<div class="tipTitle-3FYEQp">¿Sabías que...?</div>' in driver.page_source:
        print("no hay internet, esperando 30 segundos")
        time.sleep(30)
        comando()
    else:
        now = datetime.now()
        h = str(now.hour)
        m = str(now.minute)
        if len(h) == 1:
            h = f'0{h}'
        if len(m) == 1:
            m = f'0{m}'
        
        print(f'Enviando mensaje a las {h}:{m}')
        driver.find_element(By.XPATH, "//div[@aria-label='Enviar mensaje a #💎・⇄﹕economy' and @data-slate-editor='true'][@role='textbox']").click()
        driver.find_element(By.XPATH, "//div[@aria-label='Enviar mensaje a #💎・⇄﹕economy' and @data-slate-editor='true'][@role='textbox']").send_keys("<work", Keys.ENTER)
        


def automatico():
    wc = 0
    vwc = 0
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#uid_8')))\
        .send_keys(gmail)

    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#uid_11')))\
        .send_keys(password)

    WebDriverWait(driver, 2000)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'button.marginBottom8-emkd0_.button-1cRKG6.button-f2h6uQ.lookFilled-yCfaCM.colorBrand-I6CyqQ.sizeLarge-3mScP9.fullWidth-fJIsjq.grow-2sR_-F')))\
        .click()
    print("esperando a que discord cargue")
    driver.implicitly_wait(20)
    
    WebDriverWait(driver, 2000)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'button.button-12Fmur.enabled-9OeuTA.button-f2h6uQ.lookBlank-21BCro.colorBrand-I6CyqQ.grow-2sR_-F')))\
        .click()\

    print("comenzando auto-work")

    while True:
        pagina = driver.current_url
        if "channels/750887184533553153/939000588799201301" in pagina:
            comando()
        else:
            driver.get("https://discord.com/channels/750887184533553153/939000588799201301")
            print("esperando a que discord cargue")
            WebDriverWait(driver, 20)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'button.button-12Fmur.enabled-9OeuTA.button-f2h6uQ.lookBlank-21BCro.colorBrand-I6CyqQ.grow-2sR_-F')))\
                .click()\
            
            time.sleep(10)
            comando()
        wc += 1
        vwc += 1
        mwc = vwc*5/60

        print(f'------------------------------------------------------------------------------------------------------------------------\nHas enviado {vwc} "<works"\nY has ganado un aproximado de {vwc*200}\nEl bot ha trabajado {round(mwc,1)} horas')
        if wc == 6:
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@aria-label='Enviar mensaje a #💎・⇄﹕economy' and @data-slate-editor='true'][@role='textbox']").click()
            driver.find_element(By.XPATH, "//div[@aria-label='Enviar mensaje a #💎・⇄﹕economy' and @data-slate-editor='true'][@role='textbox']").send_keys("<dep all", Keys.ENTER)
            wc = 0
        time.sleep(301)

driver.implicitly_wait(10)
time.sleep(2)
if "marginTop8-24uXGp marginCenterHorz-574Oxy linkButton-2ax8wP button-f2h6uQ lookLink-15mFoz lowSaturationUnderline-Z6CW6z colorLink-1Md3RZ sizeMin-DfpWCE grow-2sR_-F" in driver.page_source:
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'button.marginTop8-24uXGp.marginCenterHorz-574Oxy.linkButton-2ax8wP.button-f2h6uQ.lookLink-15mFoz.lowSaturationUnderline-Z6CW6z.colorLink-1Md3RZ.sizeMin-DfpWCE.grow-2sR_-F')))\
        .click()
    automatico()
else:
    automatico()
