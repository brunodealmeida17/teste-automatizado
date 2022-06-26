from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from automacao.xpath import *


class AutomacaoSensorWeb():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver/chromedriver.exe')
        self.driver.maximize_window()

    def Scroll(self):
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")

        for contador in range(20):
            self.driver.execute_script(
                "window.scrollTo(0, window.scrollY + 200);")
            time.sleep(1)
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                None
            new_height = last_height
        time.sleep(1)

    def Home(self):        
        self.driver.get(xpath_SITE_LINK)
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_vantagens).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, xpath_como_funciona).click()
        time.sleep(3)                     
        self.driver.find_element(By.XPATH, xpath_area_atuacao).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, xpath_Home_banco_sangue).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_Home_laboratorio_pesquisa).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_Home_logistica_farma).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_oque_dizem).click()
        time.sleep(10)   

    def Clientes(self):
        self.driver.find_element(By.XPATH, xpath_clientes).click()
        time.sleep(5)
        self.Scroll()

    def Parceiros(self):
        self.driver.find_element(By.XPATH, xpath_parceiros).click()
        time.sleep(5)
        self.Scroll()

    def Solucoes(self):
        self.driver.find_element(By.XPATH, xpath_solucoes).click()
        time.sleep(5)
        self.Scroll()

    def Contatos(self):
        self.driver.find_element(By.XPATH, xpath_contatos).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_form_username).send_keys(
            'Bruno de Almeida MIranda')
        self.driver.find_element(By.XPATH, xpath_form_email).send_keys(
            'brunodealmeida17@hotmail.com')
        self.driver.find_element(
            By.XPATH, xpath_form_telefone).send_keys('61993069676')
        self.driver.find_element(
            By.XPATH, xpath_form_empresa).send_keys('SensorWeb')
        self.driver.find_element(
            By.XPATH, xpath_form_cargo).send_keys('processo seletivo')
        self.driver.find_element(
            By.XPATH, xpath_form_atuacao).send_keys('outro')
        self.driver.find_element(By.XPATH, xpath_form_mensagem).send_keys(
            'Teste automatizado com selenium (python) para processo seletivo ')
        self.driver.find_element(By.XPATH, xpath_form_checkbox).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300);")
        time.sleep(2)

    def Sorbrenos(self):
        self.driver.find_element(By.XPATH, xpath_sobrenos).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, xpath_elements).click()
        time.sleep(5)
        self.Scroll()

    def Blog(self):
        self.driver.find_element(By.XPATH, xpath_blog).click()
        time.sleep(5)
        self.Scroll()
        
      
       
