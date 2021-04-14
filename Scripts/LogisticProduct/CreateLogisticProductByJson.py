from ManipulateData.ReadData.ReadCsv import ReadCsv
from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv
from Models.LogisticProduct import LogisticProduct

base_sap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\arq_json.json')
saps = base_sap.dictionary('sku')

base_thoth = ReadCsv('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Csv\\ONLY_SKU_BASE_THOTH.csv')
thoth_skus_list = [x.upper() for x in base_thoth.get_dict("sku")]

acc = 0
criadas_novas = []


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
    logistic_product.codigo_barras = line_sap['codigo_barras']
    return logistic_product


lista = ["sku,bar_code,desc,tipo_de_veiculo,marca_id,cat_id"]

# sku,bar_code,tipo_de_veiculo,marca_id,cat_id

for sap_sku in saps:
    if sap_sku.upper() in thoth_skus_list:
        continue
    sap_line = saps[sap_sku]
    logisticProduct = populate_logistic_product(sap_line)
    lista.append(logisticProduct.__str__())
    acc += 1
    criadas_novas.append(f"{acc}. {sap_sku.upper()}")

print(f"qty def sku criadas: {acc}")


WriteCsv('criar_logistic_product_by_json').write_by_lines(lista)

WriteCsv("sku_que_serao_criadas").write_by_lines(criadas_novas)
