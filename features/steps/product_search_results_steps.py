from behave import when
from selenium.webdriver.common.by import By

PRODUCT_RESULTS = (By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")

@when('Navigate to the second page')
def page_click(context):
    context.app.search_results_page.page_click()


@when ('Click on the third item')
def click_third_result(context):
    context.driver.find_elements(*PRODUCT_RESULTS)[2].click()
