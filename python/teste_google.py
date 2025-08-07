from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import resolvebase64
import anticaptcha
import json

#--------------json----------------
with open('\pythonjson\contabilista.json', 'r') as file:
    dados = json.load(file)

userContabilista = dados["contabilista"]
senhaContabilista = dados["senha_contabilista"]


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://www.sefaz.mt.gov.br/acesso/pages/login/login.xhtml"
 
driver.get(url)
time.sleep(1)


driver.find_element(By.XPATtime.sleep(2))

driver.find_element(By.XPATH,'//*[@id="formLogin:selectTipoUsuario_1"]').click()
time.sleep(2)

login = driver.find_element(By.XPATH,'//*[@id="formLogin:inputLogin"]')
login.send_keys()
time.sleep(2)

senha = driver.find_element(By.XPATH,'//*[@id="formLogin:inputSenha"]')
senha.send_keys()
time.sleep(2)

#iverWait(driver, 10).until(#  EC.visibility_of_element_located((By.ID, 'formLogin:inputSenha'))

captcha = driver.find_element(By.XPATH,'//*[@id="formLogin:superPanel"]/div[3]/div/img')

pega_captcha = captcha.get_attribute("src")

resolvebase64.decode64(pega_captcha)

resposta_captcha = anticaptcha.anticaptcha()

print(resposta_captcha)

texto_captcha = driver.find_element(By.XPATH,'//*[@id="formLogin:inputCaptcha"]')
texto_captcha.send_keys(resposta_captcha)
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="formLogin:j_idt90"]/span').click()