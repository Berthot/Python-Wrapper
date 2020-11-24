import csv
import os

from ManipulateData.ReadData.Sheet import Sheet


class OpenCsv:

    def __init__(self, path, tipo='pasta'):
        self._path = path
        self._tipo = tipo
        pass

    def _lista_nome_itens_das_pastas(self):
        lista = []
        if self._tipo == 'arquivo':
            return [self._path]
        for arquivo in os.listdir(self._path):
            if arquivo == 'desktop.ini':
                continue
            try:
                pasta = f'{self._path}/{arquivo}'
                lista.append(pasta)
            except:
                raise ValueError('erro planilha: ' + arquivo)
        return lista

    @staticmethod
    def _linha_csv_dic(arqcsv, nome_planilha):
        header = []
        head = True
        array_dic = []
        for linha in arqcsv:
            if head:
                head = False
                if linha[-1] == '':
                    header = linha[:-1]
                else:
                    header = linha
                continue
            dic_linha = {}
            for key in range(len(header)):
                try:
                    head_key = header[key].lower()
                    dic_linha[head_key] = linha[key]
                except:
                    print("PLANILHA: " + nome_planilha)
                    print(f'{header} : {len(header)}')
                    print(f'{linha} : {len(linha)}')
                    raise ValueError(f'Tamanho da planilha: {nome_planilha} ignorada. tamanho = 0')
            array_dic.append(dic_linha)
        return array_dic

    def get_dictionary(self):
        nome_planilha = self._path
        count_linha = 1
        array_sheet = []
        arquivo_csv = open(nome_planilha, 'r', encoding='utf-8')
        arqcsv = csv.reader(arquivo_csv)
        count_linha += 1
        array_dic = self._linha_csv_dic(arqcsv, nome_planilha)
        if len(array_dic) < 0:
            raise ValueError(f'Tamanho da planilha: {nome_planilha} ignorada. tamanho = 0')
        sheet_name = nome_planilha.split('/')[-1]
        sheet = Sheet(sheet_name, array_dic)
        array_sheet.append(sheet)
        return array_sheet

