import pytest
import time
from selenium.webdriver.common.by import By
from Pages.login_page import Login
from Pages.inventory_page import InventoryPage


def test_inventory(driver, usuario_valido, password_valida): 
    # Abrir URL e inicar sesión
    
    loginPage = Login (driver)
    loginPage.abrir()
    loginPage.login_completo(usuario_valido, password_valida)
    
    # Verificar y validar inventario
    inventory = InventoryPage(driver)
    
    assert inventory.verificar_url(), "URL de inventario incorrecta"
    assert inventory.detectar_titulo() == "Products"
    assert inventory.detectar_productos() 
    assert len(inventory.detectar_productos()) > 0

    # Agregar primer producto al carrito e ir al carrito
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()
    
    #Logout
    inventory.hacer_logout()
    assert "https://www.saucedemo.com/" in driver.current_url
    time.sleep(3)