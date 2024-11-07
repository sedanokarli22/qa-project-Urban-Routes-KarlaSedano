import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import localizadores
from metodos import UrbanRoutesPage
import codigo




class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.routes_page = UrbanRoutesPage(cls.driver)


#PROCESO COMPLETO DE PEDIR UN TAXI

    # 1.- CONFIGURAR DIRECCION
    def test_configuration_adress(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(50)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_rout(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort(self):
        self.routes_page.click_on_get_taxi()
        self.routes_page.click_comfort()
    # 2.- INTRODUCIR TELEFONO
    def test_input_phone(self):
        self.driver.implicitly_wait(10)
        self.routes_page.set_phone()
        assert self.routes_page.get_introduce_phone_number() == data.phone_number

     # 3.- RECUPERAR EL CODIGO DEL TELEFONO
    def test_input_code(self):
        self.driver.implicitly_wait(30)
        self.routes_page.introduce_code_number()
        self.driver.implicitly_wait(30)
        self.routes_page.get_code()

    # 4.- AGREGAR METODO DE PAGO
    def test_input_card(self):
        self.driver.implicitly_wait(30)
        self.routes_page.set_card()
        self.driver.implicitly_wait(30)
        assert self.routes_page.get_input_number_card() == data.card_number
        self.driver.implicitly_wait(30)
        assert self.routes_page.get_input_cvv_card() == data.card_code

    # 5.- AGREGA MENSAJE PARA EL CONDUCTOR
    def test_send_message_driver(self):
        self.driver.implicitly_wait(15)
        self.routes_page.message_to_driver()
        assert self.routes_page.get_message() == data.message_for_driver

    # 6.- AGREGAR MANTA Y PAÑUELOS
    def test_add_blanket_scarves(self):
        self.driver.implicitly_wait(20)
        self.routes_page.order_blanket_scarves()
        assert self.routes_page.get_blanket_scarves() == True

    # 7.- AGREGAR DOS HELADOS
    def test_add_icecream(self):
        self.driver.implicitly_wait(20)
        self.routes_page.order_ice_cream()
        assert self.routes_page.get_ice_cream() == "2"

    # 8.- BUSCAR UN TAXI
    def test_search_taxi(self):
        self.driver.implicitly_wait(30)
        self.routes_page.search_taxi()

    # 9.- ESPERAR EL MODAL DEL TAXI
    def test_wait_modal_taxi(self):
        self.driver.implicitly_wait(120)
        self.routes_page.wait_modal_taxi()
        self.driver.implicitly_wait(120)
        assert self.routes_page.displayed_modal_driver() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
