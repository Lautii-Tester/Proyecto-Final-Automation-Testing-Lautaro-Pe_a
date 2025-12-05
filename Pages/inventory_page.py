import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #Importamos las condiciones esperadas para las esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait #Importamos WebDriverWait para esperas explícitas


class InventoryPage:
    URL_CURRENT = "https://www.saucedemo.com/inventory.html"
    TITLE = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTON = (By.CSS_SELECTOR, "button[data-test*=add-to-cart]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verificar_url(self):
        return self.URL_CURRENT in self.driver.current_url
    
    def detectar_titulo(self):
        return self.driver.find_element(*self.TITLE).text
    
    def detectar_productos(self):
        return self.driver.find_elements(*self.PRODUCTS)
    
    def agregar_primer_producto(self):
        primer_boton = self.driver.find_elements(*self._ADD_BUTTON)[0]
        primer_boton.click()
        return self
    
    def agregar_dos_productos(self):
        botones = self.driver.find_elements(*self._ADD_BUTTON)
        botones[0].click()
        botones[1].click()
        return self

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()
        from Pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def hacer_logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        time.sleep(3) 
        logout_link.click()
        from Pages.login_page import Login
        return Login(self.driver)