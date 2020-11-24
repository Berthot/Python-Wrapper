class Product:

    def __init__(self):
        self.id = 'default'
        self.sku = ''
        self.tail = 0
        self.vehicle_type = ''
        self.price = 0
        self.stock = ''
        self.active = ''
        self.brandName = []
        self.categoryName = []
        self.logisticProductBrandId = ''
        self.logisticProductCategoryId = ''
        self.legacy = True
        self.sap = [str(self.sku + '|1')]
        self.fullData = {}

    def logistic_print(self):
        print(f'Sku: {self.sku} |:| VehicleType: {self.vehicle_type}')

    def export_to_csv(self):
        text = f'"{self.id}",' \
               f'"{self.sku}",' \
               f'"{self.vehicle_type}",' \
               f'"{self.price}",' \
               f'"{self.stock}",' \
               f'"{self.active}",' \
               f'"{self.logisticProductBrandId}",' \
               f'"{self.logisticProductCategoryId}",' \
               '"",' \
               '"",' \
               '""'
        return text
