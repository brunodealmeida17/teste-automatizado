from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import time




class AutomacaoSensorWeb():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver/chromedriver.exe')
        self.driver.maximize_window()
        
        with open("./automacao/xpath.json", encoding="utf-8") as arquivo:
            self.dados = json.load(arquivo)

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
        time.sleep(5)

    def Home(self):        
        self.driver.get(self.dados["sensorWeb"]["xpath_site_link"])
        time.sleep(10)        
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_vantagens"]).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_como_funciona"]["xpath_page"]).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_como_funciona"]["xpath_midia"]).click()
        time.sleep(185)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_area_atuacao"]["xpath_page"]).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_area_atuacao"]["xpath_banco_sangue"]).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_area_atuacao"]["xpath_laboratorio_pesquisa"]).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_area_atuacao"]["xpath_Logistica_farmaceutica"]).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_home"]["xpath_dizem"]).click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 400);")                            
      

    def Clientes(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_clientes"]["xpath_page"]).click()
        time.sleep(5)
        self.Scroll()

    def Parceiros(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_parceiros"]["xpath_page"]).click()
        time.sleep(5)
        self.Scroll()

    def Solucoes(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_solucoes"]["xpath_page"]).click()
        time.sleep(5)
        self.Scroll()

    def Contatos(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_page"]).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_nome"]).send_keys(
            'Bruno de Almeida MIranda')
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_email"]).send_keys(
            'brunodealmeida17@hotmail.com')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_telefone"]).send_keys('61993069676')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_empresa"]).send_keys('SensorWeb')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_cargo"]).send_keys('processo seletivo')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_areaatuacao"]).send_keys('outro')
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_mensagem"]).send_keys(
            'Teste automatizado com selenium (python) para processo seletivo ')
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_contatos"]["xpath_form_checkbox"]).click()
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300);")
        time.sleep(8)
        self.Scroll()

    def Sobrenos(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_sobrenos"]["xpath_page"]).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_sobrenos"]["xpath_elements"]).click()
        time.sleep(5)
        self.Scroll()

    def Blog(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_blog"]["xpath_page"]).click()
        time.sleep(5)
        self.Scroll()
        
    def Vagas(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_vagas"]["xpath_page"]).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_vagas"]["xpath_elements"]).click()
        time.sleep(5)
        self.Scroll()
        self.Scroll
        
    def Conteudo(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_conteudo"]["xpath_page"]).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_conteudo"]["xpath_elements"]).click()
        time.sleep(5)
        self.Scroll()
    
    def Apresentacao(self):
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_page"]).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_nome"]).send_keys(
            'Bruno de Almeida MIranda')
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_email"]).send_keys(
            'brunodealmeida17@hotmail.com')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_empresa"]).send_keys('SensorWeb')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_telefone"]).send_keys('61993069676')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_areaatuacao"]).send_keys('outro')        
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_cargo"]).send_keys('outro')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_pontosdemonitoramento"]).send_keys('1')        
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_formaderegistro"]).send_keys('planilha')
        self.driver.find_element(
            By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_estado"]).send_keys('go')
        
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_mensagem"]).send_keys(
            'Teste automatizado com selenium (python) para processo seletivo ')       
        self.driver.find_element(By.XPATH, self.dados["sensorWeb"]["xpath_site_apresentacao"]["xpath_form_checkbox"]).click()
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300);")
        time.sleep(8)
        self.Scroll()
        
        
        
      
       
