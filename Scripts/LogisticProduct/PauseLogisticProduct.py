from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv
from Models.LogisticProduct import LogisticProduct

realSap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\cadastros_thoth.json')
saps = realSap.dictionary('sku')

"""
O valor Y, significa que o produto está inativo
O valor N, significa que o produto está ativo.
"""
def active(dict_line):
    if str(dict_line["desativado"]) == "N":
        return 'sim'
    else:
        return 'nao'



lista = ["sku,active"]

for x in saps:
    line = saps[x]
    text = x.upper() + ","
    text += f"{active(line)}"
    lista.append(text)

write = WriteCsv('pause_logistic_product'.upper())

write.write_by_lines(lista)
