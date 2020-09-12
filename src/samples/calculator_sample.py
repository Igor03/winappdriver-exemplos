from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# desired_caps = {}
# desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

# driver = webdriver.Remote(
#             command_executor='http://127.0.0.1:4723',
#             desired_capabilities= desired_caps)    


class CalculadoraBot():

    __APP_DEFAULT_PATH = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

    def __init__(self):
        super().__init__()
        self.driver = self.__inicializar()


    def soma_positivo(self, num_1: int, num_2: int):
        driver = self.driver
        result = None
        
        try:
            # Localizando elemento por nome
            driver.find_element_by_name(self.__parse_number(num_1)).click()
            # Localizando elemento por id
            driver.find_element_by_accessibility_id('plusButton').click()
            # Localizando elemento por nome
            driver.find_element_by_name(self.__parse_number(num_2)).click()
            # Localizando elemento por id
            driver.find_element_by_accessibility_id('equalButton').click()                    
            # Capturando resultado da operacao
            result = driver.find_element_by_accessibility_id('CalculatorResults').text.split()        
            result = int(result[2])        
        except NoSuchElementException:        
            print('Algum dos identificadores nao puderam ser localizados em: {}'
                    .format(driver.desired_capabilities['app']))
        except Exception as e:
            print('Falha desconhecida. Descricao: {}'.format(e))
        finally:
            driver.quit()
        print('Resultado: {}'.format(result))
        return result


    def __inicializar(self):
        return webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= {'app':self.__APP_DEFAULT_PATH})        


    def __parse_number(self, number:int):        
        if number >= 0 :
            if number == 1: return 'Um'
            elif number == 2: return 'Dois'
            elif number == 3: return 'Três'
            elif number == 4: return 'Quatro'
            elif number == 5: return 'Cinco'
            elif number == 6: return 'Seis'
            elif number == 7: return 'Sete'
            elif number == 8: return 'Oito'
            elif number == 9: return 'Nove'
            elif number == 0: return 'Zero'
        else: raise ValueError('Apenas numeros positivos')