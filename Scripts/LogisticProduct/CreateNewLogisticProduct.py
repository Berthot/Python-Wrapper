from ManipulateData.ReadData.ReadCsv import ReadCsv
from ManipulateData.ReadData.ReadJson import ReadJson
from ManipulateData.WriteData.WriteCsv import WriteCsv
from Models.LogisticProduct import LogisticProduct

# LOGISTIC_QUE_JA_EXISTEM

realSap = ReadJson('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Json\\cadastros_thoth.json')
saps = realSap.dictionary('sku')

sapExist = ReadCsv('C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\Data\\Csv\\LOGISTIC_QUE_JA_EXISTEM.csv')
base_thoth_dic = sapExist.get_dict("sku")

base_sap = []
for s in saps:
    base_sap.append(s.upper())


base_thoth = []
for t in base_thoth_dic:
    base_thoth.append(t.upper())


lista = ["sku"]
for x in base_sap:
    if x not in base_thoth:
        lista.append(x)

write = WriteCsv('create_New_Logistic_Product'.upper())

write.write_by_lines(lista)


