from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv

realSap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\cadastros_thoth.json')
saps = realSap.dictionary('sku')

"""
sku,codigo_fornecedor,atri_codigo_fabricante,active,fornecedor
AUAB001,-------------,F00099M187            ,sim   ,Eletropar

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

lista = ["sku,codigo_fornecedor,atri_codigo_fabricante,active,fornecedor"]


def active(dict_line):
    if str(dict_line["desativado"]) == "N":
        return 'sim'
    else:
        return 'nao'


for x in saps:
    line = saps[x]
    text = f"{x.upper()},"
    text += f"{line['cod_forncedor'].upper()},"
    text += f"nothing,"
    text += f"{active(line)},"
    text += f"{line['fornecedor'].upper()}"

    lista.append(text)

write = WriteCsv('create_provider.'.upper())

write.write_by_lines(lista)
