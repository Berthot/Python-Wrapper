class Sheet:

    def __init__(self, sheet_name, array_dic, split=','):
        self._split = split
        self._sheetName = sheet_name
        self._arrayDic = array_dic

    def __str__(self):
        return self._sheetName

    def get_header(self):
        header = []
        for key in self._arrayDic[0]:
            if key == '' or key == ' ':
                continue
            header.append(key)
        return header

    def get_dictionary(self):
        return self._arrayDic

    def get_sheet_name(self):
        return self._sheetName

    def export_in_string_line(self):
        header = self.get_header()
        output_text = ''
        for x in header:
            output_text += f'"{x}",'
        output_text = output_text[:-1] + '\n'
        for line in self._arrayDic:
            text = ''
            for h in header:
                text += f'"{line[h]}",'
            output_text += text[:-1] + '\n'
        return output_text
