class LogisticProduct:

    def __init__(self):
        self.sku = ''
        self.vehicle_type = ''
        self.price = 0
        self.stock = 0
        self.brandName = ''
        self.categoryName = ''
        self.logisticProductBrandId = ''
        self.logisticProductCategoryId = ''
        self.legacy = True
        self.ean = ''
        self.gtin = ''
        self.fornecedor = ''
        self.codigo_barras = ''
        self.fullData = {}

    # sku,bar_code,tipo_de_veiculo,marca_id,cat_id
    def __str__(self):
        return f'"{self.sku}","{self.codigo_barras}","{self.brandName} {self.categoryName}","{self.vehicle_type}","{self.logisticProductBrandId}","{self.logisticProductCategoryId}"'

    def export_in_string_line(self):
        return f'"{self.sku}","{self.vehicle_type}","{self.brandName} {self.categoryName}","{self.logisticProductBrandId }",' \
               f'"{self.logisticProductCategoryId}","{self.fornecedor}","{self.ean}","{self.gtin}"'
