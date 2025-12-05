from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test*=remove]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("cart.html"))

    def detectar_productos_en_carrito(self):
        return self.driver.find_elements(*self._CART_ITEMS)
    
    def detectar_nombres_productos(self):
        elementos_nombres = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos_nombres]
    
    def continuar_comprando(self):
        self.driver.find_element(*self._CONTINUE_SHOPPING).click()
        from Pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def remover_productos(self):
        botones = self.driver.find_elements(*self._REMOVE_BUTTONS)
        botones[0].click()
        botones[1].click()
        botones[2].click()
        return self
    
    def proceder_checkout(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        return self