from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv

realSap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\cadastros_thoth.json')
saps = realSap.dictionary('sku')

lista = ["sku,desc,active,barCode"]

"""
sku,desc,active,barCode


{
    "sku": "AUAB011",
    "cod_barras": "4047024489011",
    "cod_forncedor": "F00099M150",
    "fornecedor": "Eletropar",
    "desativado": "N"
},
O valor Y, significa que o produto está inativo
O valor N, significa que o produto está ativo.
"""


def active(dict_line):
    if str(dict_line["desativado"]) == "N":
        return 'sim'
    else:
        return 'nao'


for x in saps:
    line = saps[x]

    text = f"{x.upper()},"
    text += f"nothing,"
    text += f"{active(line)},"
    text += f"{str(line['cod_barras'])}"
    lista.append(text)

write = WriteCsv('SKU_BARCODE')

write.write_by_lines(lista)
