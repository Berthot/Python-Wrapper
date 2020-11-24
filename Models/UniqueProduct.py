import datetime


class UniqueProduct:

    def __init__(self, sku_full, attribute_set_code, title, vehicle, manufacturer, full_year, desc,
                 active=True, fuel="", first_image="", id=0, product_id=0):
        self.description = desc
        self.attribute_set_code = attribute_set_code
        self.skuFull = sku_full
        self.Id = id
        self.ProductId = product_id
        self.Active = active
        self.Tail = sku_full.split('-')[1]
        self.Title = title
        self.Vehicle = vehicle
        self.Manufacturer = manufacturer
        self.FullYear = full_year
        self.Fuel = fuel
        self.FirstImage = first_image
        self.UpdateAt = datetime.datetime.now()

    def export(self):
        line = f'"{self.skuFull.split("-")[0]}",' \
               f'"{self.Tail}",' \
               f'"{self.Vehicle}",' \
               f'"{self.Manufacturer}",' \
               f'"{self.FullYear}",' \
               f'"{self.Fuel}",' \
               f'"{self.FirstImage}",' \
               f'"{self.Title}",' \
               f'"{self.description}",' \
               f'"{self.UpdateAt}",' \
               f'"{self.Active}",'
        return f'{line}\n'
