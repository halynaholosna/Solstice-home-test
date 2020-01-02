from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

@then ('Verify Add to card button is present and clickable')
def verify_add_to_cart_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON))