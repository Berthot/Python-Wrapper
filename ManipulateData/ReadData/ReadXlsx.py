import xlrd

from Helpers.Tratamento import Tratamento
from ManipulateData.ReadData.Sheet import Sheet


class OpenXlsx:

    def __init__(self, path):
        self.__path = path
        self._tratamento = Tratamento()

    def __leitura_xlsx(self):
        try:
            planilha = xlrd.open_workbook(self.__path)
        except:
            raise ValueError(f"caminho: {self.__path} \n caminho não aceito, corrigir caminho")
        colunas = planilha.sheet_by_index(0)  # pega a sheet 1
        planilha_excel_em_lista = []
        for linha in range(colunas.nrows):  # pega valor de linhas
            valor_linha = colunas.row_values(linha)  # pega valor da linha
            planilha_excel_em_lista.append(valor_linha)
        return planilha_excel_em_lista

    def __convert_xlsx_to_dic(self):
        planilha_excel = self.__leitura_xlsx()
        head_test = False
        header = []
        lista_das_planilhas = []
        for linha in planilha_excel:
            dict_linha = {}
            if not head_test:
                header = self._tratamento.tratamento_header(linha)
                head_test = True
                continue
            for item in range(0, len(header)):
                dict_linha[header[item]] = self.__get_value_tratado(self._retirar_quebra_linha(linha[item]))
            lista_das_planilhas.append(dict_linha)
        return lista_das_planilhas

    @staticmethod
    def _retirar_quebra_linha(item):
        try:
            if "\n" in str(item):
                return item.replace("\n", "")
            else:
                return item
        except:
            print(f"type {item} is {type(item)}")
            error = f"Não Foi possivel quebrar linha {item}"
            raise ValueError(error)

    def __get_value_tratado(self, value):
        if type(value) == int or type(value) == float:
            return value
        else:
            return self.__concatenar_valor(value)

    def __concatenar_valor(self, item):
        return str(self._tratamento.tratamento_linha(item))

    def convert_one_xlsx_to_dic(self, nome_planilha):
        count_linha = 1
        array_dic = self.__convert_xlsx_to_dic()
        count_linha += 1
        if len(array_dic) < 2:
            raise ValueError("Tamanho da planilha " + nome_planilha)
        sheet_name = nome_planilha.split('/')[-1]
        return Sheet(sheet_name.replace("xlsx", 'csv'), array_dic)


# x = OpenXlsx('/home/bertho/Documents/Aut').convertOneXlsxToDic('/ficha.xlsx')
#
# for y in x:
#     print(y)
