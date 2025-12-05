import pytest 
import time
import pathlib
import logging
from selenium import webdriver
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 

#Configuración del Webdriver
@pytest.fixture (scope="function")
def driver():
    options = Options()
    options.add_argument ("--start-maximized") #Abre ventana maximizada de Edge
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(5) #Espera implícita de 5 segundos
    
    yield driver
    time.sleep (2)
    driver.quit()

#Directorios paraa REPORTS y LOGS
target= pathlib.Path("../Reports")
target.mkdir (parents=True, exist_ok=True)

path_dir = pathlib.Path ("../logs")
path_dir.mkdir (parents=True, exist_ok=True)

#Configuración de LOOGING
logging.basicConfig(
    filename = path_dir / "historial.log",
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt= "%H:%M:%S"
)
logger = logging.getLogger()

#Credenciales válidas
@pytest.fixture
def usuario_valido():
    return "standard_user"
@pytest.fixture
def password_valida():
    return "secret_sauce"

#Capturas de pantalla en caso de fallo
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    #Sólo tomar captura si el test falla en la fase "call"
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = target / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))

            #Adjuntar captura al reporte HTML
            if hasattr(report, "extra"):
               from pytest import extras
               report.extra.append(extras.png(str(screenshot_path)))

#Título personalizado para el reporte HTML
def pytest_html_report_title(report):
    report.title = "TalentoLab - Protecto Final QA Automatización"

#Configuarion de URL base para API Testing
@pytest.fixture
def URL_API():
    return "https://jsonplaceholder.typicode.com/"