from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# TODO Inserir waits para localizacao de elementos

class FortineBot():

    __APP_DEFAULT_PATH = r'E:\FortiNet\FortiClient.exe'

    def __init__(self):
        """[summary]
        """        
        super().__init__()
        self.driver = self.__inicializar()
        

    def conectar_vpn(self, vpn_number:int, username:str, password:str):
        """[summary]

        Args:
            vpn_number (int): [description]
            username (str): [description]
            password (str): [description]
        """

        driver = self.driver

        time.sleep(5)
        driver.find_element_by_name('ACESSO REMOTO').click()

        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ACESSO REMOTO"))).click()        
        
        self.__select_vpn(vpn_number)
        
        driver.find_element_by_name("Usuário {{username}}").send_keys(username)
        driver.find_element_by_name("Senha {{password}}").send_keys(password)
        driver.find_element_by_name("Conectar").click()
        
        self.__aceitar_nova_conexao()
        self.__verifica_status()        


    def __select_vpn(self, vpn_number:int, max_elements:int = 3):    
        
        driver = self.driver        
        flag_found = False
        counter_elements = 0
        __ELEMENT_NAME = "Nome da VPN {{vpnName}}"
        driver.find_element_by_name(__ELEMENT_NAME).click()
        
        for i in range(max_elements): driver.find_element_by_name(__ELEMENT_NAME).send_keys(Keys.ARROW_UP) 
        
        curr_vpn = driver.find_element_by_name(__ELEMENT_NAME).text
        curr_vpn = curr_vpn.lower().replace('vpn', '').strip()
        
        while not flag_found and counter_elements != max_elements:        
            if vpn_number == int(curr_vpn): 
                flag_found = not flag_found
                driver.find_element_by_name(__ELEMENT_NAME).send_keys(Keys.ENTER)
                continue
            
            driver.find_element_by_name(__ELEMENT_NAME).send_keys(Keys.ARROW_DOWN)
            
            curr_vpn = driver.find_element_by_name(__ELEMENT_NAME).text
            curr_vpn = curr_vpn.lower().replace('vpn', '').strip()
            
            counter_elements += 1
        if not flag_found: raise ValueError('Valor nao encontrado')
    

    def __aceitar_nova_conexao(self, opt:bool = True, max_expect:int=5):
        
        time.sleep(max_expect)
        try:
            if opt: self.driver.find_element_by_name('Sim').click()
            else: self.driver.find_element_by_name('Não').click()
        except Exception as e:
            pass
    

    def __inicializar(self):        
       
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= {'app':self.__APP_DEFAULT_PATH}) 
        # return driver    
        return webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= {'app': r'Root'})         

    def __verifica_status(self):
        
        driver = self.driver
        time.sleep(1)
        try:
            driver.find_element_by_name('Desconectar')
            print('*'*30+'\nVPN Conectada\n'+'*'*30)
        except NoSuchElementException:
            raise ValueError('Rede nao conectada a VPN')
  