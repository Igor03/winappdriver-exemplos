import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


# TODO Inserir waits para localizacao de elementos

class NotepadBot():

    __APP_DEFAULT_PATH = "notepad.exe"

    def __init__(self):
        """[summary]
        """        
        super().__init__()
        self.driver = self.__inicializar()


    def criar_arquivo(self, texto: str, caminho: str, nome:str, overwrite:bool=True):                
        """[summary]

        Args:
            texto (str): [description]
            caminho (str): [description]
            nome (str): [description]
            overwrite (bool, optional): [description]. Defaults to True.
        """        

        self.__preencher_arquivo(texto)
        self.__salvar_arquivo(caminho, nome)
        self.driver.close_app()

    
    def __inicializar(self):
        
        return webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= {'app':self.__APP_DEFAULT_PATH})     


    def __preencher_arquivo(self, text:str):
        
        driver = self.driver
        driver.find_element_by_accessibility_id('15').send_keys(text)


    def __salvar_arquivo(self, caminho:str, nome:str, overwrite:bool=True):
        
        driver = self.driver
        driver.find_element_by_name("Arquivo").click()
        driver.find_element_by_name("Salvar Como...	Ctrl+Shift+S").click()        
        
        time.sleep(1)
        
        driver.find_element_by_accessibility_id("1001").send_keys(caminho+nome)
        driver.find_element_by_name("Salvar").click()   
        self.__sobrescrever(opt=overwrite)


    def __sobrescrever(self, opt:bool=True):
        
        time.sleep(1)
        try:
            if opt: self.driver.find_element_by_name('Sim').click()
            else: self.driver.find_element_by_name('Não').click()
        except Exception as e:
            pass