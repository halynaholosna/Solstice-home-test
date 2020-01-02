from behave import given

@given ('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')