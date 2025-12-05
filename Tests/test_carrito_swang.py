import pytest
import time
from Pages.login_page import Login
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage

def test_carrito(driver, usuario_valido, password_valida): 
    # Abrir URL e inicar sesión

    loginPage = Login (driver)
    loginPage.abrir()
    loginPage.login_completo(usuario_valido, password_valida)
    
    # Verificar y validar inventario
    inventory = InventoryPage(driver)
    assert inventory.verificar_url()
    
    #Agregar 3 productos al carrito e ir al carrito
    assert inventory.detectar_productos() 
    assert len(inventory.detectar_productos()) > 0
    inventory.agregar_primer_producto()
    inventory.agregar_dos_productos()
    cart = inventory.ir_al_carrito()

    #Verificar productos en el carrito
    productos = cart.detectar_productos_en_carrito()
    assert len(productos) == 3, "El carrito no contiene 3 productos"
    nombres= cart.detectar_nombres_productos()
    print("Productos en el carrito:", nombres)

    #Continuar comprando y realizar al checkout
    inventory = cart.continuar_comprando()
    assert inventory.verificar_url()
    cart = inventory.ir_al_carrito()
    cart.proceder_checkout()

    time.sleep(3)