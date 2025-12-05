import pytest
import time
from Pages.login_page import Login
#from Data.data_login import CASOS_LOGIN
#from Utils.login_csv import get_login_csv, get_login_json
from Utils.faker_utils import generar_usuario

@pytest.mark.parametrize("usuario,contraseña,login_bool", generar_usuario())
def test_login(driver, usuario, contraseña, login_bool): #1. Testeo de login con distintas credenciales
    loginPage = Login(driver)
    loginPage.abrir()
    loginPage.completar_usuario(usuario)
    loginPage.completar_contraseña(contraseña)
    loginPage.hacer_click_login()

    if login_bool:
        assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    else:
        assert "https://www.saucedemo.com/inventory.html" not in driver.current_url

    time.sleep(3)  #Pausa de 3s para ver el login antes de continuar