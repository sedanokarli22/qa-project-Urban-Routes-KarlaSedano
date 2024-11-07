import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import phone_number, card_number, address_from, address_to, card_code, message_for_driver
from localizadores import UrbanRoutesPageLocators
import codigo




class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPageLocators

    def set_from(self, from_address):
        self.driver.find_element(*self.locators.from_field).send_keys(address_from)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_rout(self,from_address,to_address):
        self.set_from(from_address)
        self.set_to(to_address)


    def click_on_get_taxi(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.locators.button_get_taxi).click()


    def click_comfort(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.button_comfort).click()

    def click_number_button(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.button_insert_phone).click()

    def introduce_phone_number(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.insert_phone).send_keys(data.phone_number)

    def get_introduce_phone_number(self):
        return self.driver.find_element(*self.locators.insert_phone).get_property('value')

    def click_button_next_phone(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.button_next_phone).click()

    def set_phone(self):
        self.driver.implicitly_wait(30)
        self.click_number_button()
        self.introduce_phone_number ()
        self.click_button_next_phone()

    def introduce_code_number(self):
        self.driver.implicitly_wait(30)
        phone_code = codigo.retrieve_phone_code(driver= self.driver)
        self.driver.find_element(*self.locators.code_holder).send_keys(phone_code)
        self.driver.find_element(*self.locators.button_confirm_code).click()

    def get_code(self):
        return self.driver.find_element(*self.locators.code_holder).get_property('value')

    def click_card(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.payment_method).click()

    def click_add_card(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.button_add_card).click()

    def input_number_card(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.locators.input_card).send_keys(card_number)

    def click_cvv_card(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.locators.input_code).click()

    def input_cvv_card(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.locators.input_code).send_keys(card_code)

    def get_input_number_card(self):
        self.driver.implicitly_wait(20)
        return self.driver.find_element(*self.locators.input_card).get_property('value')

    def get_input_cvv_card(self):
        self.driver.implicitly_wait(20)
        return self.driver.find_element(*self.locators.input_code).get_property('value')

    def click_extra_card(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.click_out_card).click()

    def click_full_add_card(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.locators.button_full_add_card).click()

    def click_x_card(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.locators.x_button_card).click()

    def set_card(self):
        self.driver.implicitly_wait(30)
        self.click_card()
        self.click_add_card()
        self.input_number_card()
        self.input_cvv_card()
        self.click_extra_card()
        self.click_full_add_card()
        self.click_x_card()

    def message_to_driver(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.locators.driver_message).send_keys(message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.locators.driver_message).get_property('value')

    def click_requirements(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.locators.order_requirements).click()

    def order_blanket_scarves(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.locators.slider_blanket).click()

    def get_blanket_scarves(self):
        self.driver.implicitly_wait(15)
        return self.driver.find_element(*self.locators.slider_blanket_activate).is_selected()

    def order_ice_cream(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.locators.counter_ice_cream).click()
        self.driver.find_element(*self.locators.counter_ice_cream).click()

    def get_ice_cream(self):
        self.driver.implicitly_wait(15)
        return self.driver.find_element(*self.locators.select_two_ice_creams).text

    def search_taxi(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.locators.smart_button_get_taxi).click()

    def wait_modal_taxi(self):
        self.driver.implicitly_wait(60)
        return self.driver.find_element(*self.locators.modal_taxi).is_displayed()
        self.driver.implicitly_wait(60)

    def displayed_modal_driver(self):
        self.driver.implicitly_wait(60)
        return self.driver.find_element(*self.locators.image_taxi).is_displayed()




















