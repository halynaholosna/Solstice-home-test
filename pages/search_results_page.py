from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):
    SECOND_PAGE_ICON = (By.CSS_SELECTOR, "a[href*='page=2']")

    def page_click(self, *SECOND_PAGE_ICON):
        self.driver.find_element(*self.SECOND_PAGE_ICON).click()
