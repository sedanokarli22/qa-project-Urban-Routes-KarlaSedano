from selenium.webdriver.common.by import By

class UrbanRoutesPageLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_get_taxi = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    button_comfort= (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    button_insert_phone= (By.CLASS_NAME, 'np-text')
    insert_phone = (By.ID, 'phone')
    button_next_phone = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code_holder = (By.XPATH, '//*[@id="code"]')
    button_confirm_code = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_method = (By.CLASS_NAME, 'pp-text')
    button_add_card = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    input_card = (By.ID, 'number')
    input_code = (By.NAME, "code")
    click_out_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div')
    button_full_add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    x_button_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    driver_message = (By.ID, 'comment')
    order_requirements = (By.CLASS_NAME, 'reqs')
    slider_blanket = (By.CLASS_NAME, 'r-sw')
    slider_blanket_activate = (By.CSS_SELECTOR, '.r-sw > div >input')
    counter_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    select_two_ice_creams = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-value')
    smart_button_get_taxi = (By.CLASS_NAME, 'smart-button-main')
    modal_taxi = (By.CSS_SELECTOR, ".order-header-title")
    image_taxi = (By.XPATH, '//img[@src="/static/media/bender.e90e5089.svg"]')









