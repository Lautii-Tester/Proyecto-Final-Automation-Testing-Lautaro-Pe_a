from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #Importamos las condiciones esperadas para las esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait #Importamos WebDriverWait para esperas explícitas

class Login:
    
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def abrir(self):
        self.driver.get(self.URL)
        return self
    
    def completar_usuario(self, usuario):
        campo = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self
   
    def completar_contraseña(self, contraseña):
        campo = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        campo.clear()
        campo.send_keys(contraseña)
        return self
   
    def hacer_click_login(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        boton.click()
        return self
   
    def login_completo(self,usuario, contraseña):
        self.abrir()
        self.completar_usuario(usuario)
        self.completar_contraseña(contraseña)
        self.hacer_click_login()
        return self