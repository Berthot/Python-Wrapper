from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv
from Models.LogisticProduct import LogisticProduct

"""
Relatorio :

rodar logistic product no C#

"sku",
"vehicletype",
"desc",
"brandid",
"categoryid",
"codigo_fornecedor",
"ean",
"gtin",

"""

realSap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\base_produtos.json')
saps = realSap.dictionary('sku')


def populate_logistic_product(line_sap):
    logistic_product = LogisticProduct()
    if line_sap['empresa_name'].lower() == 'vsr':
        vehicle_type = 'moto'
    else:
        vehicle_type = 'carro'
    logistic_product.sku = line_sap['sku']
    logistic_product.vehicle_type = vehicle_type
    logistic_product.price = 0
    logistic_product.stock = 0
    logistic_product.brandName = line_sap['fabricante_name']
    logistic_product.categoryName = line_sap['categoria_name']
    logistic_product.logisticProductBrandId = line_sap['fabricante_code']
    logistic_product.logisticProductCategoryId = line_sap['categoria_code']
    logistic_product.legacy = True
    logistic_product.fullData = line_sap
    logistic_product.ean = line_sap['NCM']
    logistic_product.gtin = line_sap['NCM']
    logistic_product.fornecedor = line_sap['cod_forncedor']
    return logistic_product


lista = ["sku,vehicletype,desc,brandid,categoryid,codigo_fornecedor,ean,gtin"]

for sap in saps:
    sap_line = saps[sap]
    logisticProduct = populate_logistic_product(sap_line)
    lista.append(logisticProduct.export_in_string_line())

write = WriteCsv('logistic_prod_update')

write.write_by_lines(lista)
