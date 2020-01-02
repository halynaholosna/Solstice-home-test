from behave import given, when

@given ('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when ('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_for_keyword(product)