from .orderDetails import OrderDetailsPage


class DashboardPage:

    def __init__(self, page):
        self.page = page
    
    def select_product(self, product_name):
        Product = self.page.locator("//h4/a[text()='{}']/ancestor::app-card".format(product_name))
        Product.locator("button").click()

    def select_checkout(self):
        self.page.get_by_text("Checkout").click()
        ordersDetailsPage = OrderDetailsPage(self.page)
        return ordersDetailsPage

