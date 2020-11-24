import csv


class WriteCsv:

    def __init__(self, name):
        self._path = 'C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\ZOutPutData\\' + name + '.csv'

    def set_new_path(self, new_name):
        self._path = 'C:\\Users\\matheus.bertho\\Documents\\Git\\Python-Wrapper\\ZOutPutData\\' + new_name + '.csv'

    def write_by_dictionary(self, dicionary_array):
        with open(f"{self._path}", mode='w', newline='', encoding='utf-8') as write_arq_csv:
            line = ''
            header = []
            for header_one in dicionary_array[0]:
                header.append(header_one)
                line += f'"{header_one}",'

            write_arq_csv.write(line[:-1] + '\n')
            for dic in dicionary_array:
                if dic == {}:
                    continue
                line = ''
                for h in header:
                    line += f'"{str(dic[h])}",'
                write_arq_csv.write(line[:-1] + '\n')

    def write_by_lines(self, line_array):
        with open(f"{self._path}", mode='w', newline='', encoding='utf-8') as write_arq_csv:
            for line in line_array:
                write_arq_csv.write(line + '\n')

